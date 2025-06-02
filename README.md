# 🛡️ Vulnerability Assessment Agent – End-to-End Workflow

This project showcases the complete workflow of a multi-agent system designed to assess vulnerabilities on a remote system using industry-standard tools. Each "agent" represents a defined step in the process, from planning to reporting.

---

## 🔍 Project Goal

To simulate a coordinated, step-by-step vulnerability assessment process using tools like `nmap`, `nikto`, and `dirb`, structured as an automated agent flow.

---

## ⚙️ Agent Workflow Overview

### 1. 🎯 Vulnerability Assessment Strategist

* **Goal**: Define initial scan strategy
* **Tools**: `nmap`, `nikto`, `dirb`, `sqlmap`
* **Output**:

  ```bash
  nmap -A [IP]
  dirb http://[IP] -w /usr/share/dirb/wordlists/common.txt
  nikto -h [IP]
  sqlmap -u 'http://[IP]/vulnerable_page' --dbs
  ```

---

### 2. 🧠 Senior Security Reviewer

* **Goal**: Review and approve the strategy
* **Checks**: Clarity, technical soundness, ethical boundaries
* **Status**: Approved

---

### 3. 💻 Remote Command Executor

* **Goal**: Run approved commands on a remote Kali Linux machine via SSH
* **Results**:

  * ✅ `nmap`: Identified open ports & services
  * ✅ `nikto`: Found missing HTTP headers
  * ❌ `dirb`: Failed due to malformed URL

---

### 4. 📑 Command Output Analyst

* **Goal**: Review command outputs for errors and insights
* **Findings**:

  * `dirb` failed (syntax error)
  * `nmap` revealed active services (HTTP, HTTPS)
  * `nikto` flagged missing security headers

---

### 5. 🧰 Linux Error Troubleshooter

* **Goal**: Resolve execution issues
* **Solution**:

  * Corrected URL format in `dirb` command

---

### 6. 📝 Vulnerability Report Writer

* **Goal**: Summarize findings in Markdown format
* **Structure**:

  * Executive Summary
  * Key Findings
  * Recommendations

---

## 🧪 Executed Commands & Highlights

### `nmap -A [IP]`

* **Detected**:

  * Open Ports: 80/tcp, 443/tcp
  * Services: HAProxy
  * SSL Certificate: Valid (Wikimedia domain)

### `nikto -h [IP]`

* **Detected**:

  * Missing headers: `X-Frame-Options`, `X-Content-Type-Options`
  * HTTPS redirect on root page

### `dirb http://[IP] -w /usr/share/dirb/wordlists/common.txt`

* **Result**:

  * ❌ Fatal Error (invalid URL format)

---

## ✅ Final Recommendations

1. **Fix Technical Errors**

   * Correct and rerun `dirb` for full directory scan

2. **Improve Web Security**

   * Add missing HTTP security headers
   * Audit HAProxy configuration

3. **Maintain Ethical Standards**

   * Confirm explicit authorization before testing
   * Document scope and intent clearly

---

## 💡 Key Takeaways

* Demonstrates a real-world vulnerability scan flow using automated agents
* Includes strategic planning, execution, troubleshooting, and reporting
* Emphasizes not just tooling, but structured thinking and ethical awareness in cybersecurity

---
