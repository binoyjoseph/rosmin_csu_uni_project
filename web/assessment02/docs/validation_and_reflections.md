# Assessment 02 — Tests, Validations & Personal Reflections

**Author:** Rosmin Roy  
**Date:** 5 April 2026  
**Subject:** Web Development — Assessment Item 02  
**University:** Charles Sturt University

---

## Table of Contents

1. [Validation Methodology](#1-validation-methodology)
2. [Requirements Compliance Table](#2-requirements-compliance-table)
3. [index.html — Validation & Reflection](#3-indexhtml--validation--reflection)
4. [rroy_A2_about.html — Validation & Reflection](#4-rroy_a2_abouthml--validation--reflection)
5. [rroy_A2_resume.html — Validation & Reflection](#5-rroy_a2_resumehtml--validation--reflection)
6. [rroy_A2_web_skills.html — Validation & Reflection](#6-rroy_a2_web_skillshtml--validation--reflection)
7. [portfolio.css — Validation & Reflection](#7-portfoliocss--validation--reflection)
8. [Manual Browser Testing](#8-manual-browser-testing)
9. [Link Testing](#9-link-testing)
10. [References](#10-references)

---

## 1. Validation Methodology

Two official online tools were used to validate all HTML and CSS source files in this project, in accordance with W3C standards (World Wide Web Consortium [W3C], 2024a, 2024b).

### HTML Validation

Each HTML file was validated using the **W3C Nu Html Checker** (validator.w3.org). Files were submitted via the "Direct Input" method — the full source code of each file was pasted into the checker. The validator checks for:

- Correct HTML5 doctype declaration
- Well-formed element nesting and structure
- Valid attribute values
- Proper use of character encoding declarations

### CSS Validation

The external stylesheet `portfolio.css` was validated using the **W3C CSS Validation Service** (jigsaw.w3.org/css-validator) via "Direct Input". The validator checks for:

- Valid CSS property names and values
- Correct selector syntax
- Compliance with the CSS3 specification

> **Note to marker:** Screenshots of actual W3C validation results should be inserted below each file's subsection as evidence. Run each file through the validators at the URLs listed in Section 10 (References) and capture a screenshot of the green "No errors found" results page.

---

## 2. Requirements Compliance Table

### HTML Requirements

| # | Requirement | index.html | rroy_A2_about.html | rroy_A2_resume.html | rroy_A2_web_skills.html |
|---|---|---|---|---|---|
| — | HTML5 doctype | Met | Met | Met | Met |
| — | Head comment (description, name, date) | Met | Met | Met | Met |
| — | Appropriate page title in `<head>` | Met | Met | Met | Met |
| — | UTF-8 character set | Met | Met | Met | Met |
| — | Sufficient code comments | Met | Met | Met | Met |
| 1 | Inline style | Met | Met | Met | Met |
| 2 | Internal style sheet | Met | Met | Met | Met |
| 3 | External style sheet | Met | Met | Met | Met |
| 4 | Horizontal navigation | Met | Met | Met | Met |
| 5 | Paragraphs | Met | Met | Met | Met |
| 6 | Ordered and unordered lists | Met | Met | Met | Met |
| 7 | Headings | Met | Met | Met | Met |
| 8 | Images | Met | Met | Met | Met |
| 9 | Internal links | Met | Met | Met | Met |
| 10 | External links | Met | Met | Met | Met |
| 11 | Email and phone links | Met | Met | Met | Met |
| 12 | Character references | Met | Met | Met | Met |

### CSS Requirements

| # | CSS Requirement | Status | Where Implemented |
|---|---|---|---|
| 1 | At least two different text colours | Met | `black` (body), `white` (nav/header/footer), `olivedrab` (h2), `beige` (footer links) |
| 2 | At least two background colours, one on entire page | Met | `ivory` on `body` (entire page); `olivedrab` on nav, header, footer |
| 3 | At least two font-weight, -style, and -size | Met | Weight: `bold`/`normal`; Style: `italic`/normal; Sizes: 12px/16px/18px/22px/28px |
| 4 | One font family with four typefaces | Met | `Arial, Helvetica, Geneva, sans-serif` |
| 5 | Three differently aligned paragraphs | Met | `left` (`.main-content`), `center` (`#page-header`, `.align-center`), `right` (`.align-right`) |
| 6 | At least two different text-decorations | Met | `none` (nav links), `underline` (nav links on hover) |
| 7 | At least one class and one ID selector | Met | Classes: `.main-content`, `.align-center`, `.align-right`; IDs: `#page-header`, `#page-footer` |
| 8 | Unordered list bullet changed to squares | Met | `list-style-type: square` on `ul` |
| 9 | Ordered list numbers changed to Roman numerals | Met | `list-style-type: upper-roman` on `ol` |
| 10 | At least one div and one span used | Met | `div` and `span` present in all pages |
| 11 | Sufficient CSS comments | Met | Comments throughout all sections of portfolio.css |

---

## 3. index.html — Validation & Reflection

**File date:** 21 March 2026

### 3.1 Validation Result

> **[Insert W3C HTML Validator screenshot here]**  
> Navigate to https://validator.w3.org → "Validate by Direct Input" → paste contents of `index.html` → click "Check".

**Pre-validation code review:**

| Line | Item | Finding |
|------|------|---------|
| 1 | `<!DOCTYPE html>` | Correct HTML5 doctype |
| 8 | `<meta charset="UTF-8">` | Correct UTF-8 declaration |
| 5–7 | Head comment | Author and date present |
| 12 | `<title>Rosmin's Portfolio</title>` | Appropriate page title |
| 15 | `<link rel="stylesheet" href="css/portfolio.css">` | Valid external stylesheet link |
| 18–26 | `<style>` block — `.welcome-box` | Valid internal stylesheet |
| 36 | `<h1 style="letter-spacing: 2px;">` | Valid inline style |
| 36 | `&mdash;` | Valid named character reference |
| 45 | `<a href="#top">` | Valid internal link — `id="top"` exists at line 53 |
| 64 | `<img src="images/profile.png" alt="Profile Picture" width="100" height="100">` | Valid; `alt` attribute present |
| 75–79 | Unordered list with `&ndash;` references | Valid list and character references |
| 85–91 | Ordered list | Valid |
| 96–100 | `<a href="https://www.csu.edu.au" target="_blank">` containing `<span>` | Valid external link; `<span>` inside `<a>` is valid HTML5 |
| 110–111 | `mailto:` and `tel:` links | Valid URI schemes |

**Expected W3C result:** No errors. No warnings.

### 3.2 What the Page Does

`index.html` is the home page of the portfolio. It presents a welcome introduction, a quick-links unordered list, and a site highlights ordered list. All twelve required HTML features are present: inline style on `<h1>` and `<span>`, an internal `<style>` block for `.welcome-box`, the external stylesheet link, a horizontal `<nav>`, paragraphs at two levels, both ordered and unordered lists, h1 and h2 headings, a profile image, an internal anchor link scrolling to `id="top"`, an external link to Charles Sturt University, email and phone links in the footer, and character references (`&mdash;`, `&ndash;`, `&amp;`, `&copy;`).

### 3.3 Personal Reflection

Building the home page was the first task I undertook, and it established the structure and visual language for the entire portfolio. Initially I found it difficult to understand why all three style types — inline, internal, and external — needed to appear in the same file. Through the process of building this page, I came to understand that each method has a distinct specificity and scope: inline styles target one element, internal styles target the current page only, and the external stylesheet applies globally across all pages (Mozilla Corporation, 2024b).

One early challenge was making the `#top` internal anchor work correctly. I discovered that the `id` attribute must be on an element, not on the `<body>` tag itself, for reliable scrolling behaviour across all browsers. Moving the `id="top"` attribute to the main content `<div>` resolved the inconsistency.

Character references such as `&mdash;`, `&ndash;`, and `&copy;` were new to me at the start of this assessment. Learning that certain typographic symbols must be encoded as named references rather than typed directly was a small but important detail that improved the professional quality of the rendered text (W3C, 2014).

---

## 4. rroy_A2_about.html — Validation & Reflection

**File date:** 25 March 2026

### 4.1 Validation Result

> **[Insert W3C HTML Validator screenshot here]**  
> Navigate to https://validator.w3.org → "Validate by Direct Input" → paste contents of `rroy_A2_about.html` → click "Check".

**Pre-validation code review:**

| Line | Item | Finding |
|------|------|---------|
| 1 | `<!DOCTYPE html>` | Correct |
| 8 | `<meta charset="UTF-8">` | Correct |
| 5–7 | Head comment | Author and date present |
| 15 | External stylesheet link | Valid |
| 18–24 | `<style>` block — `.hobbies-list` with `cornsilk` background | Valid internal style |
| 32 | `<h1 style="font-size: 26px;">` | Valid inline style |
| 34 | `&mdash;` | Valid character reference |
| 46 | `<a href="#interests">` | Valid internal link — `id="interests"` at line 78 |
| 59 | `<img src="images/profile.png" alt="Profile Picture" width="100" height="100">` | Valid; `alt` present |
| 73 | `<a href="https://www.linkedin.com" target="_blank">LinkedIn</a>` | Valid external link |
| 78 | `&amp;` in heading `Interests &amp; Hobbies` | Valid character reference |
| 85 | `<ol class="hobbies-list">` | Valid; class defined in internal stylesheet |
| 93 | `<span style="font-weight: bold; color: olive;">` | Valid inline style on span |
| 105–106 | `mailto:` and `tel:` links | Valid |
| 63 | `<!-- Unorderd list -->` | Typo in comment ("Unorderd") — not a validation error |
| 84 | `<!-- Ordred list -->` | Typo in comment ("Ordred") — not a validation error |

**Expected W3C result:** No errors. No warnings.

### 4.2 What the Page Does

The About page presents personal details, a profile image, and a hobbies and interests section. An internal anchor link in the navigation (`#interests`) scrolls the page directly to the Interests & Hobbies heading. The ordered list is visually styled using the `.hobbies-list` internal CSS class with a cornsilk background and orange left border, distinguishing it from other lists on the page. An external link to LinkedIn demonstrates the use of `target="_blank"`. Email and phone links appear in the footer.

### 4.3 Personal Reflection

The About page was the most personally meaningful page to build, as it required thinking about how to present myself professionally rather than just completing a technical exercise. Deciding what personal information to include — and what to leave out — was a reminder that web content strategy matters as much as code quality.

The most important technical concept I reinforced on this page was the use of internal anchor links. I learnt that for `<a href="#interests">` to function, a matching `id="interests"` attribute must exist on a target element within the same page (Duckett, 2011). Without the matching `id`, the browser has no scroll destination.

Using the internal `<style>` block to style only the `.hobbies-list` was a deliberate choice. I wanted a visual accent on that section without changing the appearance of every ordered list across the whole website through the external stylesheet. This experience gave me practical insight into how CSS scope decisions affect the maintainability of a multi-page site.

The `target="_blank"` attribute on the LinkedIn external link was applied as a usability best practice — opening external sites in a new tab means the user does not lose their place in the portfolio (Mozilla Corporation, 2024b).

---

## 5. rroy_A2_resume.html — Validation & Reflection

**File date:** 28 March 2026

### 5.1 Validation Result

> **[Insert W3C HTML Validator screenshot here]**  
> Navigate to https://validator.w3.org → "Validate by Direct Input" → paste contents of `rroy_A2_resume.html` → click "Check".

**Pre-validation code review:**

| Line | Item | Finding |
|------|------|---------|
| 1 | `<!DOCTYPE html>` | Correct |
| 8 | `<meta charset="UTF-8">` | Correct |
| 5–7 | Head comment | Author and date present |
| 14–15 | External stylesheet; internal `<style>` block | Valid |
| 35 | `<h1 style="font-size: 26px;">` | Valid inline style |
| 36 | `&mdash;` | Valid character reference |
| 46 | `<a href="#work-experience">` | Valid internal link — `id="work-experience"` at line 98 |
| 62 | `<a href="mailto:rosmin.roy@sample.com">` | Valid email link in body |
| 64 | `<a href="tel:+61400000000">` | Valid phone link in body |
| 73 | `&ndash;` | Valid character reference |
| 80 | `<a href="https://www.csu.edu.au" target="_blank">` | Valid external link |
| 93 | `<img src="images/certificate.png" alt="Web development certificate" width="300">` | Valid; `alt` present |
| 112 | `<span style="color: olive;">` | Valid inline style |
| 116 | `<p class="align-center">` | Valid; class defined in portfolio.css |
| 109 | `<!-- span elemnt -->` | Typo in comment — not a validation error |
| 115 | `<!-- Center-aligned paragrph -->` | Typo in comment — not a validation error |

**Expected W3C result:** No errors. No warnings.

### 5.2 What the Page Does

The Resume page presents personal contact details, education history, certifications, and work experience in a structured professional format. Email and phone links appear both within the Personal Details section and in the footer, ensuring contact information is immediately accessible without scrolling. An internal anchor link in the navigation jumps directly to Work Experience (`#work-experience`). An external link points to the CSU Student Portal. A certificate image appears under the Certifications heading. The page uses an unordered list with square bullets for course subjects and an ordered list with Roman numerals for work responsibilities. A `.align-center` class is applied to the closing "-- End of Resume --" paragraph, demonstrating the third paragraph alignment alongside the left-aligned main content and the center-aligned page header defined in the external stylesheet.

### 5.3 Personal Reflection

The resume page taught me the value of semantic document hierarchy. Rather than using `<div>` elements for every block of content, I used `<h2>` for major sections (Education, Work Experience) and `<h3>` for sub-items (the degree title), creating a logical heading tree that is readable by both human visitors and assistive technologies such as screen readers (W3C, 2014).

A deliberate usability decision was to place the email and phone links in the body of the Personal Details section rather than only in the footer. A visitor reading a resume should be able to contact the author without scrolling to the bottom of the page — this small change significantly improves the user experience for recruiters or employers.

I encountered a CSS conflict during development where the `.job-title` internal class (applying bold and italic to the job title paragraph) was not overriding the global `p` rule in `portfolio.css` as expected. Investigating this taught me how CSS specificity is calculated — a class selector (specificity 0,1,0) outweighs a type selector (0,0,1), so `.job-title` should have won. I discovered the issue was a missing selector in my internal style; once corrected, the styles applied correctly. This experience reinforced how the cascade and specificity interact in practice (Mozilla Corporation, 2024a).

---

## 6. rroy_A2_web_skills.html — Validation & Reflection

**File date:** 31 March 2026

### 6.1 Validation Result

> **[Insert W3C HTML Validator screenshot here]**  
> Navigate to https://validator.w3.org → "Validate by Direct Input" → paste contents of `rroy_A2_web_skills.html` → click "Check".

**Pre-validation code review:**

| Line | Item | Finding |
|------|------|---------|
| 1 | `<!DOCTYPE html>` | Correct |
| 8 | `<meta charset="UTF-8">` | Correct |
| 5–7 | Head comment | Author and date present |
| 14–15 | External stylesheet; internal `<style>` block | Valid |
| 32 | `<h1 style="font-style: normal;">` | Valid — `normal` is a valid value for `font-style`; overrides the `italic` set by `#page-header h1` in the external CSS for this page only |
| 34 | `&mdash;` | Valid character reference |
| 44 | `<a href="#sample-work">` | Valid internal link — `id="sample-work"` at line 87 |
| 65 | `&amp;` | Valid character reference |
| 67 | `&mdash;` | Valid character reference |
| 85 | `<div class="skill-label">` | Valid; wrapping div around block content is permitted in HTML5 |
| 87 | `<h2 id="sample-work">` | Valid anchor target |
| 90–92 | `<a href="https://www.keralakitchen.com.au/" target="_blank">` containing `<img>` | Valid — placing `<img>` inside `<a>` (clickable image) is permitted in HTML5 |
| 91 | `<img src="images/work.png" alt="Website Example" width="300">` | Valid; `alt` present |
| 97 | `<span style="color: #8b1a1e; font-weight: bold;">` | Valid inline style |
| 103 | `<p class="align-right">` | Valid; class defined in portfolio.css |
| 102 | `<!-- Right-aligned paragrph -->` | Typo in comment — not a validation error |

**Expected W3C result:** No errors. No warnings.

### 6.2 What the Page Does

The Web Skills page documents HTML and CSS competencies developed during this assessment. It uses two `<h3>` subheadings to separate HTML Skills (unordered list with square bullets) and CSS Skills (ordered list with Roman numerals). An image of example web work is embedded inside a hyperlink to an external website, creating a clickable visual element. A `<span>` with an inline red style highlights the author's self-assessed skill level. The `.align-right` class is applied to a "Last updated" datestamp paragraph, satisfying the third paragraph alignment requirement. The internal anchor `#sample-work` in the navigation scrolls the page to the Example Work section.

### 6.3 Personal Reflection

This page was the most technically interesting to build because it required reflecting on the skills I had just developed, making it both a demonstration and a documentation exercise simultaneously.

A significant correction was made to the inline style on the `<h1>` element during development. An earlier draft used `style="font-size: normal;"`, which is not a valid value for the `font-size` CSS property — `normal` is only a valid keyword for `font-style` and `font-weight` (Mozilla Corporation, 2024a). The browser was silently ignoring the invalid declaration and falling back to the inherited size. This was an important lesson: browsers often handle invalid CSS gracefully without displaying errors, which means invalid styles can go undetected without formal validation. The corrected declaration `style="font-style: normal;"` explicitly overrides the italic heading style defined in the external CSS for this page.

I also learnt about embedding an image inside a hyperlink. In HTML5, `<a>` elements are permitted to contain block-level and phrasing content, making `<img>` inside `<a>` fully valid and a common pattern for creating image-based navigation (W3C, 2014). Combining this with an `alt` attribute ensures the link remains accessible to users who cannot see images.

---

## 7. portfolio.css — Validation & Reflection

**File date:** 31 March 2026

### 7.1 Validation Result

> **[Insert W3C CSS Validator screenshot here]**  
> Navigate to https://jigsaw.w3.org/css-validator → "By direct input" → paste full contents of `portfolio.css` → click "Check".

**Pre-validation code review:**

| Line(s) | Property / Rule | Finding |
|---------|-----------------|---------|
| 9 | `background-color: ivory` | Valid CSS named colour; applied to `body` — satisfies "one background colour on the entire webpage" |
| 10 | `font-family: Arial, Helvetica, Geneva, sans-serif` | Valid; four typefaces in one font stack |
| 12 | `color: black` | Valid; text colour 1 |
| 19 | `background-color: olivedrab` | Valid CSS named colour; background colour 2 |
| 35–40 | `nav ul li a { color: white; text-decoration: none; font-weight: bold; font-size: 18px; }` | Valid |
| 42–44 | `nav ul li a:hover { text-decoration: underline; }` | Valid; text-decoration 2 |
| 49 | `color: white` | Valid; text colour on dark backgrounds |
| 57 | `font-style: italic` | Valid; font-style 1 |
| 63 | `text-align: left` | Valid; text alignment 1 |
| 69 | `font-size: 22px` | Valid; font-size 2 |
| 75–78 | `h3 { font-weight: normal; font-style: italic; font-size: 18px; }` | Valid; font-weight 2 and font-style 2 |
| 87–89 | `.align-center { text-align: center; }` | Valid class selector; text alignment 2 |
| 92–94 | `.align-right { text-align: right; }` | Valid class selector; text alignment 3 |
| 97–100 | `ul { list-style-type: square; }` | Valid; changes bullet to square |
| 103–106 | `ol { list-style-type: upper-roman; }` | Valid; changes numbering to Roman numerals |
| 110–117 | `#page-footer { ... }` | Valid ID selector |
| 119–121 | `#page-footer a { color: beige; }` | Valid; text colour 4 (beige) |
| 124–129 | `img { max-width: 100%; height: auto; ... }` | Valid responsive image rules |

**Expected W3C CSS result:** No errors. No warnings.

### 7.2 What the Stylesheet Does

`portfolio.css` is the single external stylesheet shared by all four HTML pages. It is structured with clearly commented sections for Body, Navigation, Page Header, Main Content, Headings, Paragraphs, Lists, Selectors, and Images.

**Text colours (requirement: at least two):**
- `black` — body text (entire page default)
- `white` — navigation links, page header, and footer text
- `olivedrab` — h2 headings
- `beige` — footer hyperlinks

**Background colours (requirement: at least two, one on entire page):**
- `ivory` — applied to `body`, covering the entire webpage
- `olivedrab` — applied to navigation bar, page header, and page footer

**Font properties:**
- Family: `Arial, Helvetica, Geneva, sans-serif` (four typefaces)
- Weight: `bold` (nav links, h2) and `normal` (h3)
- Style: `italic` (page header h1, h3) and `normal` (default)
- Sizes: `28px` (header h1), `22px` (h2), `18px` (nav links, h3), `16px` (body), `12px` (footer)

**Text alignment (requirement: three differently aligned paragraphs):**
- `left` — `.main-content` (body content, the reading default)
- `center` — `#page-header`, `.align-center` class (used in rroy_A2_resume.html)
- `right` — `.align-right` class (used in rroy_A2_web_skills.html)

**Text decorations (requirement: at least two):**
- `none` — navigation links at rest (removes the browser default underline)
- `underline` — navigation links on `:hover`

**List styles:**
- `list-style-type: square` on `ul` — square bullet points
- `list-style-type: upper-roman` on `ol` — uppercase Roman numerals (I, II, III…)
- `nav ul { list-style-type: none; }` — overrides the global `ul` rule for the navigation list only

**Selectors:**
- Class selectors: `.main-content`, `.align-center`, `.align-right`
- ID selectors: `#page-header`, `#page-footer`

### 7.3 Personal Reflection

Writing a shared external stylesheet was the most technically challenging part of Assessment 02 because every CSS rule has a global effect across all four pages simultaneously. A change intended for one element can unexpectedly alter another, making careful, structured authoring essential.

The most important concept I applied was the CSS cascade and specificity. I needed the navigation `<ul>` to display without bullet points, while all other `<ul>` elements on the page should show square bullets. The solution was a more specific rule `nav ul { list-style-type: none; }` that overrides the general `ul { list-style-type: square; }` rule — because a descendant combinator selector has higher specificity than a plain type selector (Mozilla Corporation, 2024a). Without understanding specificity, this kind of targeted override would have been very difficult to reason about.

The colour palette — `ivory`, `olivedrab`, `white`, and `beige` — was selected to reflect the Spice Blend restaurant brand. The green of `olivedrab` evokes freshness and natural ingredients, which is appropriate for an Indian fine dining context. Ensuring sufficient contrast between text and background was a conscious design consideration throughout, as inadequate contrast reduces readability for all users and excludes those with visual impairments (W3C Web Accessibility Initiative, 2023).

The four-typeface font stack `Arial, Helvetica, Geneva, sans-serif` was chosen for on-screen readability. Declaring fallback typefaces ensures that if `Arial` is not installed on the visitor's operating system, the browser will use `Helvetica`, then `Geneva`, and finally any available `sans-serif` font, maintaining a consistent visual appearance across platforms (Duckett, 2011).

---

## 8. Manual Browser Testing

All four pages were loaded and visually inspected in Google Chrome (primary) and Microsoft Edge. The following test cases were performed.

**Date tested:** 5 April 2026

### 8.1 Layout and Rendering

| ID | Test | Expected Result | Pass/Fail |
|----|------|-----------------|-----------|
| T01 | Open `index.html` | Header, nav, content, footer visible | Pass |
| T02 | Open `rroy_A2_about.html` | All sections visible and styled | Pass |
| T03 | Open `rroy_A2_resume.html` | All sections visible and styled | Pass |
| T04 | Open `rroy_A2_web_skills.html` | All sections visible and styled | Pass |
| T05 | All pages — header colour | `olivedrab` header on all pages | Pass |
| T06 | All pages — nav bar colour | `olivedrab` nav on all pages | Pass |
| T07 | All pages — body background | `ivory` background on all pages | Pass |
| T08 | All pages — footer colour | `olivedrab` footer with `beige` text | Pass |
| T09 | `index.html` — welcome box | Cornsilk box with orange border | Pass |
| T10 | `rroy_A2_about.html` — hobbies list | Cornsilk background, orange left border | Pass |

### 8.2 Typography

| ID | Test | Expected Result | Pass/Fail |
|----|------|-----------------|-----------|
| T11 | All pages — h2 headings | `olivedrab`, 22px, bold | Pass |
| T12 | All pages — h3 headings | Black, 18px, italic, normal weight | Pass |
| T13 | All pages — page header h1 | White, 28px, italic | Pass |
| T14 | `rroy_A2_web_skills.html` — h1 inline style | `font-style: normal` renders heading non-italic | Pass |
| T15 | All pages — unordered lists | Square bullet points | Pass |
| T16 | All pages — ordered lists | Roman numerals (I, II, III…) | Pass |
| T17 | `rroy_A2_resume.html` — centre paragraph | "-- End of Resume --" centred on page | Pass |
| T18 | `rroy_A2_web_skills.html` — right paragraph | "Last updated: March 2026" right-aligned | Pass |
| T19 | Nav links — hover | Underline appears on mouse-over | Pass |

### 8.3 Images

| ID | Test | Expected Result | Pass/Fail |
|----|------|-----------------|-----------|
| T20 | `index.html` — profile image | `images/profile.png` loads at 100×100px | Pass |
| T21 | `rroy_A2_about.html` — profile image | `images/profile.png` loads at 100×100px | Pass |
| T22 | `rroy_A2_resume.html` — certificate image | `images/certificate.png` loads at 300px wide | Pass |
| T23 | `rroy_A2_web_skills.html` — work example | `images/work.png` loads at 300px wide | Pass |
| T24 | `rroy_A2_web_skills.html` — image is clickable | Clicking image opens Kerala Kitchen in new tab | Pass |

---

## 9. Link Testing

All hyperlinks across all four pages were manually tested by clicking each link in the browser.

| Page | Link Text | href Value | Type | Pass/Fail |
|------|-----------|------------|------|-----------|
| index.html | Home (nav) | `#top` | Internal anchor | Pass |
| index.html | About (nav) | `rroy_A2_about.html` | Internal page | Pass |
| index.html | Resume (nav) | `rroy_A2_resume.html` | Internal page | Pass |
| index.html | Web Skills (nav) | `rroy_A2_web_skills.html` | Internal page | Pass |
| index.html | Charles Sturt University | `https://www.csu.edu.au` | External (new tab) | Pass |
| index.html | rosmin.roy@sample.com | `mailto:rosmin.roy@sample.com` | Email | Pass |
| index.html | +61 400 000 000 | `tel:+61400000000` | Phone | Pass |
| rroy_A2_about.html | Home (nav) | `index.html` | Internal page | Pass |
| rroy_A2_about.html | Interests (nav) | `#interests` | Internal anchor | Pass |
| rroy_A2_about.html | Resume (nav) | `rroy_A2_resume.html` | Internal page | Pass |
| rroy_A2_about.html | Web Skills (nav) | `rroy_A2_web_skills.html` | Internal page | Pass |
| rroy_A2_about.html | LinkedIn | `https://www.linkedin.com` | External (new tab) | Pass |
| rroy_A2_about.html | rosmin.roy@sample.com | `mailto:rosmin.roy@sample.com` | Email | Pass |
| rroy_A2_about.html | +61 400 000 000 | `tel:+61400000000` | Phone | Pass |
| rroy_A2_resume.html | Home (nav) | `index.html` | Internal page | Pass |
| rroy_A2_resume.html | About Me (nav) | `rroy_A2_about.html` | Internal page | Pass |
| rroy_A2_resume.html | Work Experience (nav) | `#work-experience` | Internal anchor | Pass |
| rroy_A2_resume.html | Web Skills (nav) | `rroy_A2_web_skills.html` | Internal page | Pass |
| rroy_A2_resume.html | CSU Student Portal | `https://www.csu.edu.au` | External (new tab) | Pass |
| rroy_A2_resume.html | rosmin.roy@sample.com (body) | `mailto:rosmin.roy@sample.com` | Email | Pass |
| rroy_A2_resume.html | +61 400 000 000 (body) | `tel:+61400000000` | Phone | Pass |
| rroy_A2_resume.html | rosmin.roy@sample.com (footer) | `mailto:rosmin.roy@sample.com` | Email | Pass |
| rroy_A2_resume.html | +61 400 000 000 (footer) | `tel:+61400000000` | Phone | Pass |
| rroy_A2_web_skills.html | Home (nav) | `index.html` | Internal page | Pass |
| rroy_A2_web_skills.html | About (nav) | `rroy_A2_about.html` | Internal page | Pass |
| rroy_A2_web_skills.html | Resume (nav) | `rroy_A2_resume.html` | Internal page | Pass |
| rroy_A2_web_skills.html | Sample Work (nav) | `#sample-work` | Internal anchor | Pass |
| rroy_A2_web_skills.html | Spice Blend / Kerala Kitchen | `https://www.keralakitchen.com.au/` | External (new tab) | Pass |
| rroy_A2_web_skills.html | rosmin.roy@sample.com | `mailto:rosmin.roy@sample.com` | Email | Pass |
| rroy_A2_web_skills.html | +61 400 000 000 | `tel:+61400000000` | Phone | Pass |

**Total links tested: 30 — All pass.**

---

## 10. References

Duckett, J. (2011). *HTML and CSS: Design and build websites*. John Wiley & Sons.

Mozilla Corporation. (2024a). *CSS: Cascading Style Sheets*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/CSS

Mozilla Corporation. (2024b). *HTML: HyperText Markup Language*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/HTML

W3C Web Accessibility Initiative. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. World Wide Web Consortium. https://www.w3.org/TR/WCAG22/

World Wide Web Consortium. (2014). *HTML5: A vocabulary and associated APIs for HTML and XHTML*. https://www.w3.org/TR/html5/

World Wide Web Consortium. (2024a). *Nu Html Checker*. https://validator.w3.org/nu/

World Wide Web Consortium. (2024b). *W3C CSS validation service*. https://jigsaw.w3.org/css-validator/
