"use strict";

// When the page is served from the backend (e.g. http://127.0.0.1:8000/app/), use same origin so no CORS.
// When opened as file://, fall back to backend URL (must have backend running).
function getApiBaseUrl() {
  if (typeof window === "undefined") return "http://127.0.0.1:8000";
  if (window.API_BASE_URL !== undefined && window.API_BASE_URL !== "") return window.API_BASE_URL;
  var o = window.location;
  if (o.protocol === "http:" || o.protocol === "https:") return o.origin;
  return "http://127.0.0.1:8000";
}
const API_BASE_URL = getApiBaseUrl();

document.addEventListener("DOMContentLoaded", () => {
  const yearSpan = document.getElementById("year");
  if (yearSpan) yearSpan.textContent = new Date().getFullYear().toString();

  initNavigation();
  initSearch();
  initPractice();
  initLedger();
  initDashboard();
});

function initNavigation() {
  const pages = document.querySelectorAll(".page");
  const navLinks = document.querySelectorAll(".nav-link");

  function showPage(name) {
    const hash = name || (window.location.hash.slice(1) || "search");
    pages.forEach((p) => {
      p.classList.toggle("active", p.id === "page-" + hash);
    });
    navLinks.forEach((a) => {
      a.classList.toggle("active", a.getAttribute("data-page") === hash);
    });
  }

  window.addEventListener("hashchange", () => showPage());
  navLinks.forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const page = a.getAttribute("data-page");
      window.location.hash = page;
      showPage(page);
    });
  });
  showPage();
}

function setStatus(el, message, type) {
  if (!el) return;
  el.textContent = message;
  el.classList.remove("error", "success", "info");
  if (type) el.classList.add(type);
}

// —— Search ——
function initSearch() {
  const form = document.getElementById("search-form");
  const queryInput = document.getElementById("query");
  const resultsList = document.getElementById("results-list");
  const statusMessage = document.getElementById("status-message");

  if (!form || !queryInput || !resultsList || !statusMessage) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const query = queryInput.value.trim();
    if (!query) {
      setStatus(statusMessage, "Please enter a search term.", "error");
      resultsList.innerHTML = "";
      return;
    }
    setStatus(statusMessage, "Searching...", "info");
    resultsList.innerHTML = "";
    try {
      const url = `${API_BASE_URL}/api/search?q=${encodeURIComponent(query)}`;
      const res = await fetch(url, { method: "GET", headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      const data = await res.json();
      renderSearchResults(data, resultsList);
      setStatus(
        statusMessage,
        Array.isArray(data) && data.length > 0 ? `Found ${data.length} topic(s).` : "No topics found. Try a different search term.",
        Array.isArray(data) && data.length > 0 ? "success" : "info"
      );
    } catch (err) {
      console.error(err);
      setStatus(statusMessage, "Cannot reach the server. Make sure the backend is running.", "error");
    }
  });
}

function renderSearchResults(topics, listEl) {
  listEl.innerHTML = "";
  if (!Array.isArray(topics) || topics.length === 0) return;
  topics.forEach((topic) => {
    const li = document.createElement("li");
    li.className = "result-item";
    const title = document.createElement("div");
    title.className = "result-title";
    title.textContent = topic.name || "Untitled Topic";
    li.appendChild(title);
    const meta = document.createElement("div");
    meta.className = "result-meta";
    meta.textContent = topic.asc_reference ? `ASC Reference: ${topic.asc_reference}` : "ASC Reference: N/A";
    li.appendChild(meta);
    const links = document.createElement("div");
    links.className = "result-links";
    if (topic.oer_link) {
      const oer = document.createElement("a");
      oer.href = topic.oer_link;
      oer.target = "_blank";
      oer.rel = "noopener noreferrer";
      oer.textContent = "OER resource";
      links.appendChild(oer);
    }
    if (topic.fasb_link) {
      const fasb = document.createElement("a");
      fasb.href = topic.fasb_link;
      fasb.target = "_blank";
      fasb.rel = "noopener noreferrer";
      fasb.textContent = "FASB Codification (Basic View)";
      if (links.childNodes.length) links.appendChild(document.createTextNode(" · "));
      links.appendChild(fasb);
    }
    if (links.childNodes.length) li.appendChild(links);
    const progressWrap = document.createElement("div");
    progressWrap.className = "result-progress";
    progressWrap.innerHTML = "Track: ";
    ["viewed", "in_progress", "mastered"].forEach((status) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "progress-btn";
      btn.textContent = status.replace("_", " ");
      btn.addEventListener("click", () => logProgress(topic.id, status));
      progressWrap.appendChild(btn);
    });
    li.appendChild(progressWrap);
    listEl.appendChild(li);
  });
}

async function logProgress(topicId, status) {
  let userId = localStorage.getItem("studyhub_user_id") || "";
  if (!userId) {
    userId = prompt("Enter your User ID (used for the Dashboard):") || "anonymous";
    localStorage.setItem("studyhub_user_id", userId);
  }
  try {
    const res = await fetch(`${API_BASE_URL}/api/progress`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({ user_id: userId, topic_id: topicId, status, notes: null }),
    });
    if (res.ok) setStatus(document.getElementById("status-message"), "Progress logged.", "success");
    else setStatus(document.getElementById("status-message"), "Could not log progress.", "error");
  } catch (_) {
    setStatus(document.getElementById("status-message"), "Could not reach server.", "error");
  }
}

// —— Practice ——
function initPractice() {
  const topicSelect = document.getElementById("practice-topic");
  const practiceList = document.getElementById("practice-list");
  const practiceDetail = document.getElementById("practice-detail");
  const scenarioText = document.getElementById("practice-scenario-text");
  const tryLedgerLink = document.getElementById("practice-try-ledger");

  async function loadTopics() {
    try {
      const res = await fetch(`${API_BASE_URL}/api/practice/topics`, { headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      const data = await res.json();
      topicSelect.innerHTML = "<option value=''>Select a topic</option>" + (data || []).map((t) => `<option value="${t.id}">${escapeHtml(t.name)}</option>`).join("");
    } catch (_) {
      topicSelect.innerHTML = "<option value=''>Failed to load topics</option>";
    }
  }

  topicSelect.addEventListener("change", async () => {
    const topicId = topicSelect.value;
    practiceList.innerHTML = "";
    practiceDetail.classList.add("hidden");
    if (!topicId) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/practice?topic_id=${topicId}`, { headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      const templates = await res.json();
      templates.forEach((t) => {
        const li = document.createElement("li");
        li.className = "practice-item";
        li.innerHTML = `<button type="button" data-id="${t.id}">${escapeHtml(t.template_text.slice(0, 80))}${t.template_text.length > 80 ? "…" : ""}</button>`;
        li.querySelector("button").addEventListener("click", () => showPracticeDetail(t.id));
        practiceList.appendChild(li);
      });
    } catch (_) {
      practiceList.innerHTML = "<li>Could not load scenarios.</li>";
    }
  });

  async function showPracticeDetail(id) {
    try {
      const res = await fetch(`${API_BASE_URL}/api/practice/${id}`, { headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      const t = await res.json();
      scenarioText.textContent = t.template_text;
      tryLedgerLink.href = "#ledger";
      tryLedgerLink.dataset.templateId = id;
      practiceDetail.classList.remove("hidden");
    } catch (_) {
      scenarioText.textContent = "Could not load scenario.";
      practiceDetail.classList.remove("hidden");
    }
  }

  loadTopics();
}

// —— Ledger Simulator ——
function initLedger() {
  const templateSelect = document.getElementById("ledger-template");
  const tbody = document.getElementById("ledger-tbody");
  const addRowBtn = document.getElementById("ledger-add-row");
  const checkBtn = document.getElementById("ledger-check");
  const messageEl = document.getElementById("ledger-message");

  async function loadTemplates() {
    try {
      const res = await fetch(`${API_BASE_URL}/api/practice`, { headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      const list = await res.json();
      templateSelect.innerHTML = "<option value=''>Free-form (balance only)</option>" + (list || []).map((t) => `<option value="${t.id}">#${t.id} ${escapeHtml(t.template_text.slice(0, 50))}…</option>`).join("");
    } catch (_) {
      templateSelect.innerHTML = "<option value=''>Free-form (balance only)</option>";
    }
  }

  function addRow() {
    const tr = document.createElement("tr");
    tr.className = "ledger-row";
    tr.innerHTML = `
      <td><input type="text" class="ledger-account" placeholder="Account name" /></td>
      <td><input type="number" class="ledger-debit" placeholder="0" min="0" step="0.01" /></td>
      <td><input type="number" class="ledger-credit" placeholder="0" min="0" step="0.01" /></td>
      <td><button type="button" class="ledger-remove" aria-label="Remove row">×</button></td>
    `;
    tr.querySelector(".ledger-remove").addEventListener("click", () => tr.remove());
    tbody.appendChild(tr);
  }

  addRowBtn.addEventListener("click", addRow);
  tbody.querySelector(".ledger-remove").addEventListener("click", function () {
    if (tbody.querySelectorAll(".ledger-row").length > 1) this.closest("tr").remove();
  });

  checkBtn.addEventListener("click", async () => {
    const rows = tbody.querySelectorAll(".ledger-row");
    const entries = [];
    rows.forEach((row) => {
      const account = row.querySelector(".ledger-account").value.trim();
      const debit = parseFloat(row.querySelector(".ledger-debit").value) || 0;
      const credit = parseFloat(row.querySelector(".ledger-credit").value) || 0;
      if (account || debit || credit) entries.push({ account: account || "?", debit, credit });
    });
    if (entries.length === 0) {
      setStatus(messageEl, "Add at least one entry (account and debit or credit).", "error");
      return;
    }
    const templateId = templateSelect.value || null;
    let url = `${API_BASE_URL}/api/practice/ledger/validate?`;
    if (templateId) url += `template_id=${encodeURIComponent(templateId)}`;
    setStatus(messageEl, "Checking…", "info");
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ entries }),
      });
      if (!res.ok) throw new Error(res.status);
      const data = await res.json();
      messageEl.classList.remove("info", "error", "success");
      messageEl.classList.add(data.balanced ? (data.correct === false ? "info" : "success") : "error");
      messageEl.textContent = data.message + (data.hint ? " " + data.hint : "");
    } catch (_) {
      setStatus(messageEl, "Could not validate. Is the backend running?", "error");
    }
  });

  loadTemplates();
}

// —— Dashboard ——
function initDashboard() {
  const userIdInput = document.getElementById("dashboard-user-id");
  const loadBtn = document.getElementById("dashboard-load");
  const summaryDiv = document.getElementById("dashboard-summary");
  const viewedEl = document.getElementById("d-viewed");
  const inProgressEl = document.getElementById("d-in-progress");
  const masteredEl = document.getElementById("d-mastered");
  const activityList = document.getElementById("dashboard-activity");

  const savedUserId = localStorage.getItem("studyhub_user_id");
  if (savedUserId) userIdInput.value = savedUserId;
  userIdInput.addEventListener("change", () => localStorage.setItem("studyhub_user_id", userIdInput.value.trim()));

  loadBtn.addEventListener("click", async () => {
    const user_id = userIdInput.value.trim();
    if (!user_id) return;
    localStorage.setItem("studyhub_user_id", user_id);
    try {
      const res = await fetch(`${API_BASE_URL}/api/progress/dashboard?user_id=${encodeURIComponent(user_id)}`, { headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(res.status);
      const d = await res.json();
      viewedEl.textContent = d.topics_viewed ?? 0;
      inProgressEl.textContent = d.topics_in_progress ?? 0;
      masteredEl.textContent = d.topics_mastered ?? 0;
      activityList.innerHTML = "";
      (d.recent_activity || []).forEach((a) => {
        const li = document.createElement("li");
        li.textContent = `${a.topic_name || "Topic " + a.topic_id}: ${a.status}${a.timestamp ? " at " + new Date(a.timestamp).toLocaleString() : ""}`;
        activityList.appendChild(li);
      });
      summaryDiv.classList.remove("hidden");
    } catch (_) {
      summaryDiv.classList.add("hidden");
      alert("Could not load dashboard. Is the backend running?");
    }
  });
}

function escapeHtml(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}
