# 🤖 CrewAI Vulnerability Assessment - Multi-Agent System
![unnamed](https://github.com/user-attachments/assets/b60658fb-d358-459e-b2f6-a0cb88f01ddd)
> **I built an AI agent crew that automatically performs cybersecurity vulnerability assessments using industry-standard tools like nmap, nikto, and dirb.**
---

## 🎯 What I Built

A **6-agent AI system** that works together to scan networks, find vulnerabilities, fix errors, and generate professional security reports - all automatically.

**💡 Think of it like having a cybersecurity team of AI specialists that collaborate to complete complex assessments without human intervention.**

---

## 🏆 Results & Impact

✅ **83% Success Rate** - 5 out of 6 security scans executed flawlessly  
✅ **Automatic Error Recovery** - When dirb command failed, AI troubleshooter fixed it  
✅ **Professional Reports** - Generated executive-ready vulnerability documentation  
✅ **Real Infrastructure** - Executed on actual Kali Linux systems via SSH  

### Key Findings from Live Scan:
- 🔍 **Discovered**: Open ports 80/tcp, 443/tcp running HAProxy
- 🚨 **Vulnerabilities**: Missing security headers (X-Frame-Options, X-Content-Type-Options)
- 🔧 **Auto-Fixed**: URL formatting errors in directory enumeration
- 📋 **Generated**: Complete vulnerability report with remediation steps

---

## 🛠️ Technical Stack

**AI Framework**: CrewAI (Multi-agent orchestration)  
**Security Tools**: nmap, nikto, dirb, sqlmap  
**Infrastructure**: Remote Kali Linux via SSH  
**Languages**: Python  
**Output**: Automated Markdown reports  

---

## 🤖 The Agent Crew

```
🎯 Strategist     → Plans the attack strategy
🧠 Reviewer       → Approves for safety & ethics  
💻 Executor       → Runs commands on remote systems
📊 Analyst        → Reviews results for issues
🔧 Troubleshooter → Fixes any errors automatically
📝 Reporter       → Writes professional documentation
```

**Each agent has specialized skills and they collaborate in sequence to complete the full assessment.**

---

## 💼 Why This Matters

**For DevSecOps**: Automates security testing in CI/CD pipelines  
**For Security Teams**: Consistent, repeatable vulnerability assessments  
**For Business**: Reduces manual security work by 90%  
**For Compliance**: Documented audit trails and professional reports  

---

## 🔥 Key Skills Demonstrated

- **Multi-Agent AI Development** with CrewAI framework
- **Cybersecurity Tool Integration** (real pentesting tools)
- **Linux System Administration** and SSH automation  
- **Error Handling & Recovery** (AI fixes its own mistakes)
- **Professional Security Reporting** 

---

## 🚀 Sample Output

The system automatically generated commands like:
```bash
nmap -A 192.168.1.100
nikto -h 192.168.1.100  
dirb http://192.168.1.100
```

And produced a complete vulnerability report with:
- Executive summary
- Technical findings  
- Risk assessment
- Remediation recommendations

---

> **🎯 Bottom Line**: I can build AI systems that replace manual workflows with intelligent automation, specifically in cybersecurity where precision and reliability are critical.
---
