# Security Policy

## 🔐 Security Policy

Thank you for helping keep **SuperMart Billing Software** secure.

This document explains how to report security vulnerabilities and what information should be included when reporting a security issue.

## 📌 Supported Versions

Currently, the latest version of the project is the actively maintained version.

| Version        | Supported |
| -------------- | --------- |
| Latest         | ✅ Yes     |
| Older versions | ❌ No      |

## 🚨 Reporting a Security Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

Please **do not publicly disclose the vulnerability through a GitHub Issue** before it has been reviewed.

Instead, contact the project maintainer privately through the contact information available on the GitHub profile.

### Please Include

When reporting a vulnerability, provide:

* A clear description of the vulnerability
* Steps required to reproduce the issue
* Potential impact of the vulnerability
* Relevant screenshots or error messages
* Suggested solution, if available
* Python and operating system versions, if relevant

### Example Report

```text
Title: Security vulnerability in billing application

Description:
Describe the security issue clearly.

Steps to Reproduce:
1. Start the application.
2. Perform the required action.
3. Observe the security issue.

Expected Behavior:
Explain what should happen.

Actual Behavior:
Explain what actually happens.

Potential Impact:
Explain how the issue could affect the application or its users.
```

## 🛡️ Security Best Practices for Contributors

Contributors should follow these practices:

* Never commit passwords or credentials.
* Never commit API keys or authentication tokens.
* Never include private customer information.
* Do not upload `.env` files containing secrets.
* Do not commit personal or confidential data.
* Keep third-party dependencies updated.
* Validate user input where applicable.
* Avoid executing untrusted input.
* Review code before submitting a Pull Request.

## 🔑 Sensitive Information

Never store sensitive information directly in the source code.

For example, avoid:

```python
password = "myPassword123"
```

Instead, sensitive configuration should be kept outside the source code and excluded from Git using `.gitignore`.

## 📦 Dependencies

The project currently uses Python and Pillow.

Dependencies should be obtained from trusted sources and kept reasonably up to date.

Install project dependencies using:

```bash
pip install -r requirements.txt
```

## 🐛 Security Issues vs. General Bugs

Please use the appropriate reporting method:

**Security vulnerability:**
Report privately to the project maintainer.

**General bug:**
Create a GitHub Issue with detailed reproduction steps.

**Feature request:**
Create a GitHub Issue describing the proposed feature.

## ⚠️ Scope

This security policy applies to the **SuperMart Billing Software** project and its source code.

This is an educational desktop application and should not be assumed to provide production-grade security for handling real customer, payment, or financial information without additional security controls.

## 📅 Policy Updates

This security policy may be updated as the project evolves and additional features are introduced.

---

Thank you for helping improve the security and reliability of **SuperMart Billing Software**. 🔐
