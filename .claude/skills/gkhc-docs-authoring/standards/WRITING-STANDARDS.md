# GitKraken Documentation Writing Standards

**Status:** Normative. This is the governing standard for all automated prose rewrites and all automated alt-text generation in the GitKraken docs automation system.

**Derivation.** §1–§8 are synthesized from four Google technical writing courses (below). §9 restates GitKraken's own writing rubric, AI-giveaways checklist and naming conventions (internal `gitkraken-marketing-os` repo), with the house rulings that reconcile the two. Both apply to every page.

The Google courses:

| Course | Short code used in citations |
|---|---|
| Technical Writing One | TW1 |
| Technical Writing Two | TW2 |
| Tech Writing for Accessibility | A11Y |
| SEO Starter Guide (Search Central bundle) | SEO |

The source PDFs are in `standards/sources/`:
`google-technical-writing-one.pdf`, `google-technical-writing-two.pdf`, `google-tech-writing-accessibility.pdf`, `google-seo-starter-guide.pdf`.

**How to read this document.**

- **HARD** (§2) = mechanically checkable. A linter or a deterministic rewrite pass can decide pass/fail. IDs are `H-n`.
- **One numbering.** `gkdocs lint` and the help center skill's checker report findings under these IDs, and only these. §2.11 lists the rules they check and each one's severity. A new lint rule gets its row here first.
- **SOFT** (§3) = requires judgment. A model or a human decides. IDs are `S-n`.
- Blockquotes are **verbatim Google wording**. Anything not in a blockquote is our restatement or our extension.
- Anything marked **[EXTENSION]** is *not* Google's wording and must never be attributed to Google.

**Precedence, in order:**

1. **Clarity.** TW1 states this as an absolute:
   > "In technical writing, clarity takes precedence over all other rules."
   Any rule below that reduces clarity in a specific instance yields.
2. **Accessibility.** Where accessibility and SEO conflict, accessibility wins (§7).
3. **Factual accuracy.** No rule may be satisfied by inventing content. See §8, H-79.
4. Everything else.

---

## §1 Numeric limits

Every explicit numeric threshold stated in the four courses, in one table.

| # | Limit | Google's verbatim wording | Source | Mechanically checkable? |
|---|---|---|---|---|
| N1 | **5 words** max between a noun and its pronoun | "Place the pronoun as close as possible to the referring noun. In general, if more than five words separate your noun from your pronoun, consider repeating the noun instead of using the pronoun." | TW1 | Yes — token distance |
| N2 | **3–5 sentences** ideal paragraph; **~7** ceiling | "Readers generally welcome paragraphs containing three to five sentences, but will avoid paragraphs containing more than about seven sentences." | TW1 | Yes — sentence count |
| N3 | **1-sentence** paragraphs, in quantity, indicate broken organization | "If your document contains plenty of one-sentence paragraphs, your organization is faulty." | TW1 | Detect: yes. Fix: no |
| N4 | **2 sentences** max per table cell | "Avoid putting too much text into a table cell. If a table cell holds more than two sentences, ask yourself whether that information belongs in some other format." | TW1 | Yes |
| N5 | **1 paragraph's worth** of information max per diagram; alternative test **5 bullets** | "As a rule of thumb, don't put more than one paragraph's worth of information in a single diagram. (An alternative rule of thumb is to avoid illustrations that require more than five bulleted items to explain.)" | TW2 | Bullet count: yes. Paragraph's worth: no |
| N6 | **1 idea** per sentence | "Focus each sentence on a single idea, thought, or concept. Just as statements in a program execute a single task, sentences should execute a single idea." | TW1 | No |
| N7 | **1 topic** per paragraph | "A paragraph should represent an independent unit of logic." | TW1 | No |
| N8 | **0** level-3 headings immediately after a level-2 heading | "Avoid placing a level three heading immediately after a level two heading" | TW2 | Yes |
| N9 | **0** en dashes | "Don't use." (Google style guide entry on en dashes, quoted in full) | TW1 | Yes — character class |
| N10 | Acronym threshold: define only if used "many times" **and** "significantly shorter" | "Don't define acronyms that would only be used a few times." / "Do define acronyms that meet both of the following criteria: The acronym is significantly shorter than the full term. The acronym appears many times in the document." | TW1 | No — no count given |
| N11 | Alt text: **short phrase or 1–2 sentences** | "Briefly summarize the image's purpose. Use a short phrase or one or two sentences. Long descriptions interrupt the reading flow for screen reader users." | A11Y | Yes — sentence count |
| N12 | Contrast **4.5:1** small text | "WCAG suggests these minimum contrast ratios: 4.5:1 for small text" | A11Y | Yes — tooling |
| N13 | Contrast **3:1** large text, where large = **14 pt bold / 18 pt regular** | "3:1 for large text (at least 14 pt bold / 18 pt regular)" | A11Y | Yes — tooling |
| N14 | Meta description: **1–2 sentences** | "the meta description tag, which is typically a succinct, one- or two-sentence summary of the page." | SEO | Yes |
| N15 | Directory-based URL organization matters only above **"a few thousand URLs"** | "If you have more than a few thousand URLs on your site, how you organize your content may have effects on how Google crawls and indexes your site." | SEO | Yes — corpus size |

### 1.1 Negative findings — read this before adding any threshold

These are places where Google states **no limit**, or where a limit you might expect simply does not exist in the source. Inventing a number here and attributing it to Google is a documentation defect. Treat this subsection as binding.

| # | Finding | Evidence |
|---|---|---|
| **NEG-1** | **Neither Technical Writing One nor Technical Writing Two states a maximum sentence length in words.** Google's short-sentence guidance is entirely qualitative — "one sentence = one idea." **Any word-count sentence threshold we enforce is our own invention and must be labelled [EXTENSION], never attributed to Google.** | TW1/TW2, exhaustive scan |
| **NEG-2** | **No character or word count exists for alt text anywhere in the accessibility course.** The only operative limit is ≤ 2 sentences (N11). Google's own "too wordy" rejected example runs 27 words, which is illustrative, not normative. | A11Y |
| **NEG-3** | **No page word-count target exists.** > "The length of the content alone doesn't matter for ranking purposes (there's no magical word count target, minimum or maximum, though you probably want to have at least one word)." Also flagged as a warning sign: > "Are you writing to a particular word count because you've heard or read that Google has a preferred word count? (No, we don't.)" | SEO |
| **NEG-4** | **No ideal number of links per page.** > "There's no magical ideal number of links a given page should contain. However, if you think it's too much, then it probably is." | SEO |
| **NEG-5** | **No ideal number of headings per page.** > "There's also no magical, ideal amount of headings a given page should have. However, if you think it's too much, then it probably is." | SEO |
| **NEG-6** | **No `<title>` character limit** appears in the SEO bundle. The detailed title-link page is referenced but not included. | SEO |
| **NEG-7** | **No image filename rule** exists in either the accessibility or SEO document. The only signal is Google's example filename `enchiladas-in-shopping-cart.jpg`. "Lowercase, hyphenated, descriptive filenames" is a defensible **[EXTENSION]**, not a quotation. | A11Y + SEO |
| **NEG-8** | **The accessibility course contains essentially nothing about motion, animation, GIFs, autoplay, flashing, captions, transcripts, audio description, or `prefers-reduced-motion`.** Its only motion-adjacent content is a link to an external video. See §5. | A11Y |
| **NEG-9** | **Neither the accessibility nor the SEO document specifies table accessibility markup** — no `<th>`, `scope`, or `<caption>` rules. TW1 supplies *authoring* rules for tables (N4, H-45, H-46) but no markup semantics. | A11Y + SEO |
| **NEG-10** | **The accessibility course never uses the words "idiom" or "figure of speech."** Its nearest guidance is "US-based slang, pop-cultural references." The anti-idiom rule (H-9) comes from **TW1**, not from the accessibility course. Cite it correctly. | A11Y |
| **NEG-11** | **The acronym threshold has no number** — "a few times" versus "many times" is left undefined (N10). | TW1 |
| **NEG-12** | **E-E-A-T is explicitly not a ranking factor.** > "Thinking E-E-A-T is a ranking factor. No, it's not." Do not build scoring around it. | SEO |
| **NEG-13** | **Keywords in the domain or URL path are near-worthless for ranking.** > "From a ranking perspective, the keywords in the name of the domain (or URL path) alone have hardly any effect beyond appearing in breadcrumbs." | SEO |

---

## §2 HARD rules

Mechanically checkable. Each rule states the imperative, the test, and a compact before/after where the source provides one.

### 2.1 Words and terminology

| ID | Rule | Test | Example |
|---|---|---|---|
| H-1 | Define an unfamiliar term on first use, or link to an existing definition. | First occurrence of a glossary term has neither a definition nor a link. | > "If the term already exists, link to a good existing explanation. (Don't reinvent the wheel.)" |
| H-2 | Use exactly one name per concept for the whole document. Never switch synonyms. | Build a term map on first pass; any second surface form for the same referent fails. | Before: "Protocol Buffers provide their own definition language… And that's why protobufs have won so many county fairs." After: "Protocol Buffers (or protobufs for short) provide their own definition language… And that's why protobufs have won so many county fairs." |
| H-3 | On first use of an unfamiliar acronym, spell out the full term, then the acronym in parentheses, and **bold both**. | Regex + state machine on first occurrence. | "This document is for engineers who are new to the **Telekinetic Tactile Network** (**TTN**)…" |
| H-4 | After defining an acronym, use only the acronym. | Any post-definition occurrence of the expanded form fails. | > "Do not cycle back-and-forth between the acronym and the expanded version in the same document." |
| H-5 | Never use a pronoun before introducing its noun. | Pronoun with no antecedent earlier in the paragraph. | > "Only use a pronoun after you've introduced the noun; never use the pronoun before you've introduced the noun." |
| H-6 | Keep a pronoun within 5 words of its noun (N1). | Token distance > 5 → repeat the noun. | — |
| H-7 | If a second noun intervenes between the noun and its pronoun, repeat the noun. | Noun-phrase count between antecedent and pronoun ≥ 1. | "Be careful when using Frambus or Carambola with HoobyScooby or BoiseFram because a bug in **their** core may cause accidental mass unfriending." — fails |
| H-8 | Replace `this`/`that` with the noun, or place a noun immediately after it. | Bare `This`/`That` as sentence subject. | Before: "…generates a user ID. **This** lets users authenticate to the app." After: "**This user ID** lets users authenticate." |
| H-9 | Remove idioms and culturally specific references. (Rule source is **TW1**, not the accessibility course — see NEG-10.) | Idiom dictionary. | "a piece of cake" / "Bob's your uncle" → "this task is done"; "sticky wicket" → "challenging problem"; "Be that as it may" → "However". > "Do not require readers to understand the intricacies of NASCAR, cricket, or sumo in order to understand how a piece of software works." |
| H-10 | Write in the second person. Use "you", never "we". | `we`/`our`/`us` referring to the reader. | > "Write in the second person. Refer to your audience as 'you', not 'we'." |
| H-11 | Format code-related text in code font. | Bare identifiers, paths, flags, commands outside code spans. | > "Format code-related text as code font." |
| H-12 | Never describe people without disabilities as "normal" or "healthy". | Term blocklist. | > "Better: nondisabled person, sighted person, hearing person, person without disabilities, neurotypical person." |
| H-13 | Never use terms that project judgment about a disability. | Blocklist: *victim of*, *suffering from*, *wheelchair-bound*. | > "Better: experiencing, living with, uses a wheelchair" |
| H-14 | Never use terms that remove personhood. | Blocklist: *the disabled*. | > "Better: people with disabilities" |
| H-15 | Never convey information using a visual cue alone — color, pattern, image, font styling, or a directional word. | Flag any instruction whose only identifying information is a direction (left/right/top/bottom/above/below/corner) or a color, with no accessible name (button label, menu item, field name) present. | > "don't rely exclusively on the visual elements, such as the following: colors / patterns / images / font styling / directional words (for example, 'top-right corner')" — and the fix is **additive**: > "Instead, use a mix of these visual elements and accompany them with descriptive text to convey information." So "Click **Save** in the top-right corner" passes; "Click the button on the right" fails. |

### 2.2 Voice

| ID | Rule | Test | Example |
|---|---|---|---|
| H-16 | Write the vast majority of sentences in active voice. | Passive ratio per document. Note the rule is "sparingly," not "never." | > "The vast majority of sentences in technical writing should be in active voice." / "Use the active voice most of the time. Use the passive voice sparingly." |
| H-17 | Detect passive voice with the formula: form of *be* + past participle, optionally followed by a preposition. | > "passive verb = form of be + past participle verb". Forms of *be*: is/are, was/were. Participles: verb + `-ed`, plus irregulars "sat", "known", "frozen". Trailing preposition is a corroborating clue: "was interpreted as", "is generated by", "was formed by", "is frozen by". | Active: "The cat sat on the mat." Passive: "The mat was sat on by the cat." Actorless passive: "The mat was sat on." |
| H-18 | **Exception, must be encoded:** do not classify imperative-initial sentences as passive. | Sentence begins with a bare imperative verb → active. | > "Sentences that start with an imperative verb are typically in active voice… The implied actor is you." "Click the Submit button." scores **Active**. |
| H-19 | Check every verb in a sentence, not just the first. | Per-clause classification. | "Performance metrics are required by the team, though I prefer wild guesses." = Passive, Active. > "ensure that all parts end up as active voice." |
| H-20 | Flag scientific-report passive openers. | String patterns. | > "It has been suggested that…" / "Data was taken…" / "Statistics were calculated…" / "Results were evaluated." |
| H-21 | Conversion pattern: target + verb + actor → actor + verb + target. | Deterministic rewrite once H-17 fires. | "The flags weren't parsed by the Mungifier." → "The Mungifier didn't parse the flags." · "A wrapper is generated by the Op registration process." → "The Op registration process generates a wrapper." · "Only one experiment per layer is selected by the Frombus system." → "The Frombus system selects only one experiment per layer." · "Quality metrics are identified by asterisks; ampersands identify bad metrics." → "Asterisks identify quality metrics; ampersands identify bad metrics." |

### 2.3 Sentences

| ID | Rule | Test | Example |
|---|---|---|---|
| H-22 | Flag weak and generic verbs. | Blocklist: forms of *be* (is, are, am, was, were), *occur*, *happen*. **Caveat that must be encoded:** > "a form of be is sometimes the best choice of verb, so don't feel that you have to eliminate every form of be from your writing." Never run this as an absolute. | "The exception occurs when dividing by zero." → "Dividing by zero raises the exception." · "This error message happens when…" → "The system generates this error message when…" · "We are very careful to ensure…" → "We carefully ensure…" |
| H-23 | Eliminate sentence-initial "There is" / "There are". | Regex on sentence start. Three sanctioned repairs: delete it; promote the true subject; invent the missing subject. | "There is a variable called met_trick that stores the current accuracy." → "The met_trick variable stores the current accuracy." · "There are two disturbing facts about Perl you should know." → "You should know two disturbing facts about Perl." · "There is no guarantee that the updates will be received in sequential order." → "Clients might not receive the updates in sequential order." |
| H-24 | Delete filler phrases. | Dictionary substitution. This is the only rule where Google supplies a literal lookup table. | "at this point in time" → "now" · "determine the location of" → "find" · "is able to" → "can" · "causes the triggering of" → "triggers" · "provides a detailed description of" → "describes" · "In spite of the fact that" → "Although" · "enhances the clarification of" → "clarifies" · "causes the production of" → "produces" |
| H-25 | Reserve *which* for nonessential clauses and *that* for essential clauses. Comma before *which*; no comma before *that*. | Regex + comma check. | Nonessential: "Python is an interpreted language, which Guido van Rossum invented." Essential: "Fortran is perfect for mathematical calculations that don't involve linear algebra." Read-aloud test: > "If you read a sentence aloud and hear a pause just before the subordinate clause, then use which. If you don't hear a pause, use that." |
| H-26 | Trigger a list conversion when a long sentence contains *or*, or an embedded enumeration. (Trigger is HARD; the conversion itself is S-9.) | Detect *or* / comma-series inside a long sentence. | Before: "To alter the usual flow of a loop, you may use either a break statement (which hops you out of the current loop) or a continue statement (…)." After: "To alter the usual flow of a loop, call one of the following statements: • `break`, which hops you out of the current loop. • `continue`, which skips past the remainder of the current iteration of the current loop." |
| H-27 | Flag subjective adjectives and adverbs. | Adjective/adverb intensifier list. > "Refactor amorphous adverbs and adjectives into objective numerical information." **See H-79: at GitKraken the rewriter flags but must not fabricate the number.** | Before: "Setting this flag makes the application run screamingly fast." After: "Setting this flag makes the application run 225-250% faster." |
| H-28 | Detect stacked subordinate clauses and split. | Keyword list (Google's, explicitly "by no means complete"): *which, that, because, whose, until, unless, since*. Operational heuristic: **two stacked subordinate clauses is the signal to split; one is usually fine.** | KEEP: "Python is an interpreted language, which means that the language can execute source code directly." SPLIT: "Bash is a modern shell scripting language that takes many of its features from KornShell 88, which was developed at Bell Labs." |
| H-29 | Place conditions before instructions. | Sentence-order check: "If X, do Y" — not "Do Y if X". | > "Place conditions before instructions, not after." |

### 2.4 Punctuation

| ID | Rule | Test | Example |
|---|---|---|---|
| H-30 | Use the serial (Oxford) comma. | Comma before final conjunction in a series of 3+. | "Our company uses C++, Python, Java, and JavaScript." Google's own preference note: > "we actually prefer circumventing the controversy by converting embedded lists into bulleted lists." |
| H-31 | Place a comma between a condition and its consequence. | Regex on `If …` clauses. | "If the program runs slowly, try the `--perf` flag." (with or without "then") |
| H-32 | No comma splices. | Two independent clauses joined by a comma. | Not recommended: "Samantha is a wonderful coder, she writes abundant tests." Recommended: "Samantha is a wonderful coder. She writes abundant tests." |
| H-33 | A semicolon joins only two grammatically complete, highly related sentences. | Both sides must parse as complete sentences. Flip test: > "ask yourself whether the sentence would still make sense if you flipped the thoughts to opposite sides of the semicolon." | Recommended: "Rerun Frambus after updating your configuration file; don't rerun Frambus after updating existing source code." Not recommended: "…configuration file; not after updating existing source code." |
| H-34 | Never use semicolons to separate embedded-list items. | Semicolons inside an in-sentence series. | Not recommended: "Style guides are bigger than the moon; more essential than oxygen; and completely inscrutable." Recommended: same with commas. |
| H-35 | Place a comma after a transition word that follows a semicolon. | Regex `;\s*(however|therefore|…)\s` without a following comma. | "Even seemingly trivial code changes can cause bugs; therefore, write abundant unit tests." |
| H-36 | Never use en dashes. | Character `–` present anywhere → error. | > "Don't use." |
| H-37 | End any sentence introducing a list or table with a colon, not a period. | Last character before a list/table block. | > "In technical writing, use a colon to alert readers that a list or table will follow." A short embedded list needs no colon: "My three favorite programming languages are Python, Java, and anything other than C++." |
| H-38 | Period placement with parentheses. | If the parentheses hold a whole sentence, period inside; otherwise outside. | "(Incidentally, Protocol Buffers make great birthday gifts.)" · "Binary mode relies on the more compact native form (described later in this document)." |
| H-39 | Hyphenate compound terms; in three-word compounds, hyphenate between words 1 and 2 only. | Dictionary/glossary lookup. | "Self-attention", "N-gram", "Decision-making system", "Floating-point feature" |

### 2.5 Lists and tables

| ID | Rule | Test | Example |
|---|---|---|---|
| H-40 | Numbered lists for ordered items; bulleted lists for unordered items. | > "If you rearrange the items in a bulleted list, the list's meaning does not change. If you rearrange the items in a numbered list, the list's meaning changes." | Numbered: "1. Stop the server. 2. Edit the configuration file. 3. Restart the server." |
| H-41 | Convert embedded (run-in) lists into bulleted or numbered lists. | Comma series of 3+ verb phrases inside one sentence. | Before: "The llamacatcher API enables callers to create and query llamas, analyze alpacas, delete vicunas, and track dromedaries." After: lead-in + four bullets. |
| H-42 | Keep list items parallel across **five** axes: grammar, logical category, capitalization, punctuation, **and voice**. | Per-axis comparison against item 1. Voice consistency is explicitly part of parallelism. | Parallel: "• Carrots • Potatoes • Cabbages". Fails on fragment: "• Broccoli inspires feelings of love or hate. • Potatoes taste delicious. • Cabbages." Fails on voice: "• The red dots represent sick trees. • Immature trees are represented by the blue dots. • The green dots represent healthy trees." |
| H-43 | Start every item in a numbered list with an imperative verb. | POS tag of first token. | Parallel: "1. Download the Frambus app… 2. Configure the Frambus app's settings. 3. Start the Frambus app." Nonparallel: "1. Instantiate the Froobus class. 2. Invoke the Froobus.Salmonella() method. 3. The process stalls." |
| H-44 | Capitalize the first letter of each list item. Qualified: > "(with some exceptions)". | First character case. | "• Loops • Conditionals • Variable declarations" |
| H-45 | End-punctuate list items only if they are sentences. | Sentence detection per item. | "1. Open the program. 2. Click the settings icon." |
| H-46 | Introduce every list and table with a lead-in sentence ending in a colon. | Preceding block must exist and end in `:`. | > "Terminate the introductory sentence with a colon rather than a period." |
| H-47 | Label every table column with a meaningful header. | Header row present and non-generic. | > "Label each column with a meaningful header. Don't make readers guess what each column holds." |
| H-48 | Max 2 sentences per table cell (N4). | Sentence count per cell. | — |

### 2.6 Paragraphs

| ID | Rule | Test | Example |
|---|---|---|---|
| H-49 | Keep paragraphs to 3–5 sentences; never exceed about 7 (N2). | Warn > 5, fail > 7. | > "Very long paragraphs form a dreaded 'wall of text' that readers ignore." |
| H-50 | Do not leave runs of one-sentence paragraphs (N3). | Consecutive 1-sentence paragraph count. | > "Seek ways to combine those one-sentence paragraphs into cohesive multi-sentence paragraphs or possibly into lists." |

### 2.7 Headings

| ID | Rule | Test | Example |
|---|---|---|---|
| H-51 | Tag headings with real heading elements, never with bold or large text. | No pseudo-headings. | > "Tag headings with heading elements. HTML: `<h1>`, `<h2>`, `<h3>` … Markdown: `#`, `##`, `###` …" |
| H-52 | Use a level-1 heading for the page title or main content heading. | Exactly one h1. **See §8.2 for the GitKraken adaptation — our h1 comes from frontmatter, not from body markdown.** | > "Use a level-1 heading for the page title or main content heading." |
| H-53 | Never skip heading levels. | Level delta > 1 on descent. | > "Don't skip levels of the heading hierarchy. For example, don't jump from an `<h1>` to an `<h3>`." |
| H-54 | Never stack headings. Put at least a short introduction under each heading (N8). | `###` immediately after `##` with no intervening prose. | Before: `## Creating the site` directly followed by `### Running the carambola command`. After: `## Creating the site` + "To create the site, you run the `carambola` command-line tool. The command displays a series of prompts to help you configure the site." + `### Running the carambola command` |

### 2.8 Links

| ID | Rule | Test | Example |
|---|---|---|---|
| H-55 | Link text must be informative and must make sense read out of context. | **Merged blocklist from both sources:** *Click here*, *Learn more*, *Read more*, *This document*, *website*, *article*. | > "Use informative link text to ensure that your audience hears meaningful information, not just 'Learn more, learn more, learn more.'" Good: "Learn how to format tables." (link on the phrase, period outside) |
| H-56 | Apply the out-of-context test. | Extract every anchor string on the page, strip surrounding prose, require each to be self-identifying. | > "Try reading only the anchor text (out of context) and check if it's specific enough to make sense by itself. If you don't know what the page could be about, you need more descriptive anchor text." |
| H-57 | Anchor text must not be excessively long. | Anchor length bound; no sentence-long anchors. | Bad: `<a>Knitted Cow invites local residents of Wisconsin to their grand re-opening by also offering complimentary cow-shaped ice sculptures</a>`. Better: `<a>Knitted Cow invites local residents of Wisconsin</a>` with the rest outside the anchor. |
| H-58 | Never chain links adjacent to each other. | Two `<a>` elements separated only by whitespace. | > "Don't chain up links next to each other; it's harder for your readers to distinguish between links, and you lose surrounding text for each link." Bad: `<a>so</a> <a>many</a> <a>times</a> <a>this</a> <a>year</a>`. |
| H-59 | Never emit an empty link. | `<a href>…</a>` with no text and no image with alt. | > "Bad (empty link text): `<a href="https://example.com"></a>`" Do not rely on Google's `title`-attribute fallback. |
| H-60 | Links must be real `<a href="…">` elements. | Parseable: `<a href="…">`, including with `onclick`/`class`. Not parseable: `<a routerLink="…">`, `<span href="…">`, `<a onclick="goto(…)">`, `<a href="javascript:…">`. | — |
| H-61 | Every page you care about must have at least one inbound internal link. | Site link-graph check. | > "Every page you care about should have a link from at least one other page on your site." |

### 2.9 Alt text (mechanical subset — full treatment in §4)

| ID | Rule | Test |
|---|---|---|
| H-62 | Emit an `alt` attribute on every `<img>`, without exception. | Attribute presence. Missing ≠ empty. |
| H-62a | **[EXTENSION]** Alt text is never a filename. | Alt equals the basename or ends in an image extension. A filename in the alt slot gives a screen-reader user what a missing attribute would (§4.2). |
| H-63 | Non-empty alt text is at most 2 sentences (N11). | Sentence count. |
| H-64 | Alt text must not begin with "Image of" or "Photo of". | `^(image\|photo)\s+of\b` (Google's literal prohibition). Extending to picture/graphic/screenshot/icon/diagram is **[EXTENSION]**. |
| H-65 | Capitalize the first word; end with a period. | First char uppercase; last char `.` (or `?`/`!`). |
| H-66 | No all caps in alt text. | Case check. |
| H-67 | Alt text must not duplicate the adjacent prose. | Token-overlap similarity with the immediately preceding/following sentence below threshold. |
| H-68 | Identical source images resolve to identical alt strings. | Dedupe by image hash across the corpus. |
| H-69 | Never use the `longdesc` attribute. | Attribute presence → fail. |
| H-70 | `alt=""` is permitted only when the image is decorative **and** is not the sole content of a link. | `a > img:only-child[alt=""]` → fail. See §7 X-3. |
| H-71 | Alt text must not carry the introduction ("The following diagram shows…"). That belongs in body prose. | Leading-phrase pattern. |

### 2.10 Document structure

| ID | Rule | Test | Example |
|---|---|---|---|
| H-72 | Open with an explicit scope statement. | Presence in the first paragraph. | > "A good document begins by defining its scope. For example: This document describes the design of Project Frambus." |
| H-73 | Add a non-scope statement, limited to topics the audience would reasonably expect. | Presence. | > "This document does not describe the design for the related technology, Project Froobus." Failure mode Google flags: "…or cover the history of the Linux operating system." — > "No reasonable user would expect the document to cover the history of the Linux operating system." |
| H-74 | State the audience explicitly, including prerequisite knowledge or reading. | Presence. | > "This document assumes that you understand matrix multiplication and the fundamentals of backpropagation." / "You must read 'Project Froobus: A New Hope' prior to reading this document." |
| H-75 | Every introduction states three things: what the document covers, expected prior knowledge, what it does not cover. | Presence of all three. | Model intro (verbatim): > "This document explains how to publish Markdown files using the Froobus system. Froobus is a publishing system that runs on a Linux server and converts Markdown files into HTML pages. This document is intended for people who are familiar with Markdown syntax. To learn about the syntax, see the Markdown reference. You also need to be comfortable running simple commands in a Linux terminal. This document doesn't include information about installing or configuring a Froobus publishing system. For information on installing Froobus, see Getting started." |
| H-76 | Explain *why* before asking the reader to act. | Order check: rationale block precedes the numbered steps. | > "Before you ask your reader to perform a task, explain to them why they are doing it." |
| H-77 | Limit each outline step to one concept or one specific task. | One heading = one task. | > "Limit each step of your outline to describing a concept or completing a specific task." |
| H-78 | Place the caption after the diagram. | Caption node follows the image node. | > "By convention, the caption always follows the diagram." |
| H-79 | **[EXTENSION — GitKraken override]** Never invent a factual claim, number, version, keyboard shortcut, menu path, or measurement to satisfy any other rule. Flag and escalate instead. | Any numeric or product-specific claim not present in the source text → reject the rewrite. | Applies especially to H-27, where Google's exemplar rewrite ("225-250% faster") supplies a figure the source sentence did not contain. |

### 2.11 What the linter checks

`gkdocs lint` (`src/lint/rules.ts`) and the `gkhc-docs-authoring` skill's checker
(`scripts/prose_rules.py`, a port) check this subset, with these severities. Both pass the same
cases, `src/lint/conformance.json`, which also pins this table. An **error** fails the lint, the
skill's checker and `gkdocs check`; a **warning** is read and either fixed or left with a reason
the editorial pass records. Heuristic rules are warnings, because a pattern cannot parse a sentence.

| ID | Severity | What is checked |
|---|---|---|
| H-15 | warn | Position- or colour-only references to UI ("the button on the right", "the purple circle") |
| H-30 | warn | A three-item series with no serial comma ("A, B and C"). Heuristic: a comma that closes an introductory clause or phrase ("If …,", "By default,") is skipped |
| H-36 | warn | En dashes |
| H-48 | warn | Table cells over two sentences |
| H-49 | warn | Paragraphs over seven sentences |
| H-51 | error | A paragraph that is only bold text (`**Requirements and limits**`). A bold lead-in ending in a colon before a list, and a run-in label with its text on the same line, pass |
| H-52a | error | A level-1 heading in the body |
| H-53 | warn | Skipped heading levels |
| H-54 | warn | A level-3 heading straight after a level-2 |
| H-55 | warn | Vague link text |
| H-62 | error | An image with no `alt` attribute |
| H-62a | error | Alt text that is a filename |
| H-63 | error | Alt text over two sentences (an error since 2026-11-18; it was a warning) |
| H-64 | warn | Alt text that opens with "Image of", "Screenshot of" and the like |
| H-90 | error | A product's internal terms (HOUSE-4) |
| H-91 | warn | Narration of the document (R-10) |
| H-92 | warn | Padding, officialese and commercialese (R-14) |
| H-93 | warn | Negative contractions in prose (HOUSE-2) |
| H-94 | warn | AI-giveaway vocabulary (R-17) |
| H-95 | warn | Product source paths in prose or comments (HOUSE-7) |
| H-96 | error | A product's internal-only syntax (HOUSE-7) |
| H-97 | error | A sentence or list item that starts with a numeral (HOUSE-3) |

Before 2026-11-18 the linter ran some of these under its own, shifted IDs: H-60 (now H-62), H-61
(H-63), H-62 (H-64), H-63 (H-62a), H-70 (H-55), H-40 (H-49), H-46 (H-48), H-30 for en dashes (H-36)
and H-11 (H-15). Records written before then use the old IDs.

---

## §3 SOFT rules

Require judgment. Apply with a model or a human reviewer; do not gate a build on them.

### 3.1 Prose quality

| ID | Rule | Guidance |
|---|---|---|
| S-1 | Prefer simple words. | > "prefer simple words over complex words; avoid obsolete or overly-complex English words. Sesquipedalian and rare words repel some readers." Motivation: > "a significant percentage of technical readers are more comfortable in languages other than English." |
| S-2 | Do not create acronyms for terms used only a few times (N10). | > "acronyms are really just a layer of abstraction; readers must mentally expand recently learned acronyms to the full term… so the 'shorter' acronym actually takes a little longer to process than the full term." |
| S-3 | Define technical terms on first use if they are not commonly understood. | > "Use active voice and short sentences, and define your technical terms on first use if they are not commonly understood." |
| S-4 | Avoid unfamiliar jargon, US-based slang, and pop-cultural references. | > "Avoid unfamiliar jargon, US-based slang, pop-cultural references, and complicated linguistic constructions." |
| S-5 | Never leave a sentence without an identifiable actor. | > "Good sentences in technical documentation identify who is doing what to whom." |
| S-6 | One idea per sentence (N6). | Before: "The late 1950s was a key era for programming languages because IBM introduced Fortran in 1957 and John McCarthy introduced Lisp the following year, which gave programmers both an iterative way of solving problems and a recursive way." After: four short sentences. |
| S-7 | Never mix marketing into educational content. | > "When your readers expect education, provide education; don't intersperse publicity or sales material inside educational material." |
| S-8 | Person-first language by default, but respect community preference. | > "While person-first language is generally preferred… some people prefer identity-first language; for example, this preference is common in Deaf and neurodivergent communities (Deaf person, neurodivergent person)." |
| S-9 | Execute the prose→list conversion triggered by H-26. | Judgment about item boundaries and lead-in wording. |
| S-10 | Prefer lists over long paragraphs. | > "If possible, change long paragraphs to lists to make information easier to scan." Also: > "Keep list items parallel." |
| S-11 | Match formality to context. | > "the contributor guide for a new open source project… might adopt a more informal and conversational style, while the developer guide for a commercial enterprise application might adopt a more formal style." |

### 3.2 Paragraphs and organization

| ID | Rule | Guidance |
|---|---|---|
| S-12 | The opening sentence must state the paragraph's central point. | > "Busy readers focus on opening sentences and sometimes skip over subsequent sentences." Diagnosed failure: opening a clustering paragraph with "The Pythagorean Theorem states that…". Fix: "Different clustering algorithms measure distances differently." Escape hatch: > "not all great paragraphs start with a sentence that states the theme. Starting a paragraph with a rhetorical question, for example, can engage readers." |
| S-13 | One topic per paragraph; delete or move off-topic sentences (N7). | > "When revising, ruthlessly delete (or move to another paragraph) any sentence that doesn't directly relate to the current topic." |
| S-14 | Every paragraph answers what / why / how. | > "1. What are you trying to tell your reader? 2. Why is it important for the reader to know this? 3. How should the reader use this knowledge?" |
| S-15 | Front-load the key points. | > "Imagine that your peers might only read the first paragraph of your document. Therefore, ensure that the start of your document answers your readers' essential questions." |
| S-16 | Keep the opening paragraph free of trivia. | Diagnosed failure: a v1-vs-v2 opener ending "Tidal information won't change." — > "The final sentence (about tides) isn't important enough to appear in the opening paragraph." |
| S-17 | Use scope as a live editing filter. | > "When reviewing your first draft, delete any sections that don't help satisfy the scope statement." |
| S-18 | Compare and contrast against something the reader already knows. | > "This new app is similar to the Frambus app, except with much better graphics." |
| S-19 | Introduce information at the point of maximum relevance; push project history to the end. | > "your reader probably doesn't need to know… about the history of the project in the introductory sections… If you feel the history of the project is useful, then include a link to this type of information at the end of your document." |
| S-20 | Alternate concept and practice. | > "Documents that alternate between conceptual information and practical steps can be a particularly engaging way to learn." |
| S-21 | Disclose information progressively. | Four techniques, verbatim: introduce terminology near the instructions that rely on it; > "Break up large walls of text… aim to introduce tables, diagrams, lists, and headings where appropriate."; > "Break up large series of steps… re-arrange them into shorter lists that explain how to complete sub-tasks."; start simple and add complexity. |
| S-22 | Prefer task-based headings over tool- or term-based headings. | Rejected: "Running the carambola command", "Initializing the Froobus framework". Preferred: "Creating the site". |
| S-23 | Provide the six navigation elements. | > "introduction and summary sections • a clear, logical development of the subject • headings and subheadings that help users understand the subject • a table of contents menu that shows users where they are in the document • links to related resources or more in-depth information • links to what to learn next" |
| S-24 | Choose long-vs-short document form by content type and reader experience. | > "How-to guides, introductory overviews, and conceptual guides often work better as shorter documents when aimed at readers who are new to the subject matter." vs. > "In-depth tutorials, best practice guides, and command-line reference pages can work well as lengthier documents…" |

### 3.3 Audience

| ID | Rule | Guidance |
|---|---|---|
| S-25 | Apply the documentation equation. | > "good documentation = knowledge and skills your audience needs to do a task − your audience's current knowledge and skills" |
| S-26 | Identify the audience's role first, then their proximity to the knowledge. | > "Roles, by themselves, are insufficient for defining an audience. That is, you must also consider your audience's proximity to the knowledge." And: > "Time also affects proximity." |
| S-27 | Counter the curse of knowledge. | > "Experts often suffer from the curse of knowledge, which means that their expert understanding of a topic ruins their explanations to newcomers." |
| S-28 | As audience breadth grows, explain more. | > "As your target audience widens, assume that you must explain more." |
| S-29 | Write for the audience, not yourself. | > "You must create explanations that satisfy your audience's curiosity rather than your own." |
| S-30 | Build a persona and review the draft against it — but don't over-fit. | > "relying too heavily on a persona (or two) can result in a document that is too narrowly focused to be useful to the majority of your readers." |

### 3.4 Illustrations and sample code

| ID | Rule | Guidance |
|---|---|---|
| S-31 | Write the caption before creating the illustration. | > "Then, create the illustration that best represents the caption. This process helps you to check that the illustration matches the goal." |
| S-32 | Captions are brief, state the takeaway, and focus attention. | > "They are brief. Typically, a caption is just a few words." / > "They explain the takeaway. After viewing this graphic, what should the reader remember?" |
| S-33 | The illustration must depict everything the caption claims. | Google downgrades a figure because > "although the caption refers to both content and a pointer, the illustration shows pointers but does not show content." A separate figure is rejected as > "pretty, but information-free". |
| S-34 | Constrain information per diagram (N5). | > "Just as you avoid overly-long sentences, strive to avoid visual run-ons." Research basis: > "providing any graphics—good or bad—makes readers like the document more; however, only instructive graphics help readers learn." |
| S-35 | Decompose complex systems: big picture first, then per-subsystem diagrams. | > "After showing the 'big picture,' provide separate illustrations of each subsystem." |
| S-36 | Add a visual cue or callout to focus attention. Per **HOUSE-1** (§7.1), use the standard teal accent (`#01FEE0`, 3 px stroke, corners matching the highlighted element or 5 px); no shape or number pairing required. The accompanying prose must name the control. | > "Callouts in pictures are often better than paragraph long explanations of the pictures because callouts focus the reader's attention on the most important aspects of the picture." |
| S-37 | Differentiate diagram categories by shape, pattern, line weight, or label — not color. | > "consider incorporating design elements such as different shapes, line weights, patterns, or text labels to clearly differentiate the categories." Model answer: > "Each category has a unique shape (trapezoid, circle, triangle, rectangle) and a text label (A, B, C, D)." |
| S-38 | Export generated diagrams as SVG. | > "it is usually best to export the files as Scalable Vector Graphics (SVG). The SVG format easily scales diagrams based on space constraints…" |
| S-39 | Sample code must be correct, concise, testable, and prescriptive of best practice. | > "Good samples are correct and concise code that your readers can quickly understand and easily reuse with minimal side effects." Criteria: > "Build without errors. / Perform the task it claims to perform. / Be as production-ready as possible… / Follow language-specific conventions." Never trade correctness for brevity: > "always prefer correctness over conciseness." |
| S-40 | Use named parameters in samples. | Best: `MyLevel = go.so.Level(rank=5, dimension=28, opacity=48)`. > "omitting parameter names makes it harder for novices to learn." |
| S-41 | Put anything that should travel with a copy-pasted snippet into code comments; put lengthy concept explanations before the snippet. | > "readers who copy-and-paste a snippet gather not only the code but also any embedded comments." |
| S-42 | Explain how to run the sample and what it outputs. | > "Writers should consider describing the expected output or result of sample code, especially for sample code that is difficult to run." |
| S-43 | Provide a range of sample complexity. | > "Resist the temptation to rush towards very complex sample programs, bypassing the beginner and intermediate sample programs that newcomers crave." |

### 3.5 Process and governance

| ID | Rule | Guidance |
|---|---|---|
| S-44 | Apply the editing-for-brevity checklist to every rewrite. | > "To help your audience understand your document, apply these basic editing principles: • Use active voice instead of passive voice. • Consider using simpler words that mean the same thing. • Include links to background information. • Break long sentences into shorter sentences or lists." This is the single highest-value rewrite rubric in the corpus; TW2 demonstrates it cutting roughly 75% of a bloated paragraph's words. |
| S-45 | Apply the accessibility editing checklist. | > "• Simplify: Use short sentences. • Use active voice… • Include lists… • Know your audience… • Check terminology… • Provide background information… • Edit: Request a review or peer edit from someone who is familiar with your subject matter." |
| S-46 | Scan for the three self-editing accessibility pitfalls. | > "poor or missing headings; uninformative link text; dense, complex text." |
| S-47 | QA the finished draft against its own introduction. | > "Does your introduction provide an accurate overview of the topics you cover? You might find it useful to think of this review as a form of documentation quality assurance (QA)." |
| S-48 | Read the draft aloud, or have a screen reader voice it. | > "Listen for awkward phrasing, too-long sentences, or anything else that doesn't feel natural." |
| S-49 | Test the rendered output three ways: zoom, keyboard-only, screen reader. | Named tools: ChromeVox for ChromeOS, VoiceOver for Mac. |
| S-50 | Verify contrast with a checker (N12/N13). | Google's named tool: WebAIM Contrast Checker. |
| S-51 | Apply accuracy, quality, and relevance standards to auto-generated metadata, **including alt text**. | > "focus on accuracy, quality, and relevance, especially when automatically generating the content. This includes metadata like `<title>` elements, meta description elements, structured data, and alternate texts for images, which can appear in Search results." |
| S-52 | Do not mass-generate pages without adding value. | > "using generative AI tools or other similar tools to generate many pages without adding value for users may violate Google's spam policy on scaled content abuse." |
| S-53 | Disclose automation where a reader would reasonably wonder how the content was made. | > "AI or automation disclosures are useful for content where someone might think 'How was this created?' Consider adding these when it would be reasonably expected." |
| S-54 | Keep content current, but do not fake freshness. | > "Are you changing the date of pages to make them seem fresh when the content has not substantially changed?" |

---

## §4 Alt text

This is the load-bearing section. The system generates alt text for roughly 2,500 screenshots. Google Search Central's own guidance on auto-generated "alternate texts for images" links back to the accessibility course, which settles the question of authority: **the accessibility rules are the specification; SEO inherits them and adds no conflicting requirement.**

### 4.1 Definitions and purpose

> "Alternative text (alt text) is short, descriptive text that acts as a substitute for visual items on a page. The most common use is for describing images."

> "Alt text acts as a functional equivalent of an image for readers who can't view the image."

> "Every image requires an alt text element. Alt text acts as a functional equivalent for an image by providing a concise summary of the image's purpose and context."

Two stated purposes:
> "Screen readers read alt text for people who are blind or who have low vision."
> "Descriptive alt text also helps to improve search results for images."

SEO frames the same field differently but compatibly:
> "Alt text is a short, but descriptive piece of text that explains the relationship between the image and your content."

### 4.2 The empty-vs-missing distinction

This distinction is the single most common defect and must be encoded explicitly.

| State | Markup | Screen reader behavior | Verdict |
|---|---|---|---|
| **Missing attribute** | `<img src="x.png">` | Reads the filename aloud | **Always a defect** (H-62) |
| **Empty attribute** | `<img src="x.png" alt="">` | Ignores the image entirely | Valid **only** for decorative images that are not links (H-70) |
| **Populated** | `<img src="x.png" alt="…">` | Reads the description | Default for all informative images |

> "If you don't include alt text for an image, then screen readers read the filename aloud instead of ignoring the image. A user of a screen reader has no information to indicate whether the image contains useful information."

Consequence for our pipeline: an image emitted without `alt=` will be announced as `screenshot_2024_final_v3.png`. This also argues, as defense in depth, for human-readable generated filenames — but note **NEG-7**: no filename rule exists in the source, so treat that as **[EXTENSION]**.

### 4.3 Decorative images

> "If the meaning of your document would be the same without the image, add an empty alt text attribute to the image (alt=""). Assistive technologies ignore the empty attribute."

The two enumerated situations, verbatim:

1. > "The image is decorative (not informative), such as an image of a horizontal line that is meant to be a visual border at the end of a page."
2. > "The image duplicates information that is already expressed in text on the page."

Corollary Google gives for case 1:
> "Consider making a decorative image a CSS background image, since background images are always ignored by screen readers."

**Decision procedure:** would the meaning of the document be identical if the image were deleted? If yes → `alt=""`. **For a product help center this is almost never true.** Product screenshots are informative. Reserve `alt=""` for dividers, spacers, and ornamental chrome. And never on an image that is the sole content of a link (H-70, §7 X-3).

### 4.4 Context dependence — alt text cannot be generated from the image alone

> "Explain images in the context of the text."
> "In the context of the surrounding text, you might choose to emphasize or omit aspects of an image in your description."

Google's worked example uses the **same photograph** of a black-capped chickadee on a snowy branch in two contexts:

| Surrounding text | Correct alt text | Google's reasoning |
|---|---|---|
| A passage about mixed-species flocks led by chickadees and titmice | `alt="A chickadee perched on a branch."` | > "the time of year, the specific type of chickadee, or details about the appearance of the chickadee are not important for that purpose. Alt text that identifies the bird species is sufficient." |
| A passage about how chickadees conserve energy in winter by fluffing their feathers | `alt="A black-capped chickadee perched on a snowy branch with fluffed feathers."` | > "the type of chickadee and its appearance in winter are relevant, so the alt text description should include those aspects of the image." |

**Pipeline requirement:** the alt-text generator must receive the surrounding paragraph as input. An image-only generator cannot satisfy this rule.

### 4.5 Length, formatting, and phrasing

| Rule | Wording |
|---|---|
| Length (N11) | > "Briefly summarize the image's purpose. Use a short phrase or one or two sentences. Long descriptions interrupt the reading flow for screen reader users." |
| No lead-in nouns | > "Don't include extra words like 'Image of' or 'Photo of.'" |
| Capitalization and period | > "Capitalize the first word and include a final period." / > "Use other punctuation as necessary." |
| Rationale for the period | > "Screen readers generally pause for periods and some other types of punctuation. Although a final period is not technically required, it provides auditory separation between the image description and the body text that follows the image." |
| No all caps | > "Avoid all caps." Two stated reasons: > "Words in all caps always have a rectangular shape, whereas words in regular case have distinct shapes. Some people with visual or cognitive disabilities rely more on the shape of words to read them." and > "Screen readers might misread words in all caps as acronyms." |
| No duplication | Section heading is literally "Avoid duplicating the surrounding text." Restating the adjacent paragraph makes the screen reader user hear the same content twice. |
| No introduction | > "Introduce diagrams in the body text, not in the alt text." Alt text is not the place for "The following diagram shows…". |
| Consistency | > "For repeated images, use consistent alt text." The same UI element on 40 pages gets one canonical string, not 40 variants. |
| People | > "When you describe people, include demographic information only if it is critical to the main point of the image. Otherwise, use *person* or another term that provides key context about the person's activity or role in the image, such as *musician*, *basketball player*, *teacher*, or *doctor*." |

**NEG-2 restated:** there is no character or word count. Two sentences is the only Google-attributable limit.

### 4.6 Every alt-text example in the source

Google's format is a three-way contrast: **too concise / too wordy / just right.**

| Image | Too concise | Too wordy | Just right |
|---|---|---|---|
| Photo of waffles | `alt="Waffles."` | `alt="Photo of a round white plate with 17 slices of red strawberries surrounding a stack of three golden-brown waffles with two whole red strawberries on top, with leaves."` | `alt="A stack of waffles on a plate with strawberries."` |
| Go gopher mascot (context: "The Go gopher is the mascot of the Go programming language.") | `alt="Gopher."` | `alt="Drawing of blue Go gopher with large round eyes, small yellow paws, single white tooth, and pink hat with small tassel, blowing noisemaker with orange and yellow stripes."` | `alt="Go gopher with noisemaker and 10th anniversary party hat."` |
| Person using Google Cardboard | `alt="Google Cardboard user."` | `alt="Person wearing gray and white striped shirt with orange cuffs, holding Google Cardboard viewer in front of eyes, with teeth exposed."` | `alt="Person looking into Google Cardboard viewer and smiling."` |
| Line graph, US per-capita energy use 1650–2010 | `alt="United States Per Capita Energy Use."` | `alt="Line graph showing per capita energy use in the United States from the year 1650 through the year 2000, showing a large increase after 1900 with the peak between 1970 and 1980."` | `alt="United States per capita energy use increased sharply after 1900 and peaked around 1975."` |

Two generalizations the generator must encode:

1. **"Too concise" failures are bare noun phrases** that restate the subject with no information — "Waffles.", "Gopher.", "United States Per Capita Energy Use." For a screenshot, `alt="Settings dialog."` is exactly the same failure.
2. **"Too wordy" failures enumerate colors, counts, clothing, and irrelevant physical detail.** Note the energy-use example especially: for a data graphic the "just right" answer states **the takeaway**, and does not even use the words "line graph," while the rejected version does. For screenshots of charts or graphs, generate the conclusion, not the chart mechanics.

Also note Google's own "too wordy" waffles example begins with "Photo of a…", double-flagging H-64.

### 4.7 Complex images

> "The information in a complex image such as a flowchart, graph, or map can be difficult to describe in a few short sentences. In this situation, provide a short description of the image in the alt text and a longer textual description in the main text of your document or on a separate page that you link to."

Sub-rules:
- > "For graphs, you can provide a data table on the same page or on a separate page."
- > "For flowcharts and diagrams, explain the process or parts of your image in the text of your document."

Google's real worked example (the Cloud "Software supply chain threats" page):
- Alt text: `A diagram that shows entry points for software supply chain attacks.`
- > "The body text introduces the image, explains the use of the image legend, and then explains each section of the diagram in context."

**If the long description is not adjacent to the image, name its location inside the alt text:**

> "In situations where the image and the detailed description aren't close together, specify the location of the detailed description in the alt text."

```
alt="Route map with rest stop locations. Rest stop locations are listed under
Taking breaks during your ride."
```

**Never use `longdesc`:**
> "Avoid using the longdesc attribute to describe complex images. The longdesc attribute is not well supported by screen readers. The attribute is also an obsolete feature in the HTML Living Standard."

### 4.8 Images that contain text

Neither document gives a rule of the form "transcribe text in images." The governing rules are indirect but unambiguous:

- SEO: > "Googlebot can only find content that is textually visible." / > "Make sure that your visual content is expressed in text form." / > "Put key information in text, not graphics, on the site."
- SEO's failure example: > "a product category page that contains a list of images of shirts with no textual context about each image is suboptimal. The product category page should include some textual explanation for each image."
- A11Y: complex images get a short alt plus a full description in body text (§4.7).

**Operative standard:** if an image contains text that carries meaning — an error message, a command, a config value, a menu path — that text must appear in the **body prose**, not only in the image and not crammed into alt text. Alt text summarizes; the body carries the content. A page that is a wall of screenshots with no prose steps fails both accessibility and SEO.

### 4.9 Alt text as anchor text

When an image is the entire content of a link, its alt text **is** the link's accessible name and its anchor text.

> "For images as links, Google uses the alt attribute of the img element as anchor text, so be sure to add descriptive alt text to your images"

Good:
```html
<a href="/add-to-cart.html"><img src="enchiladas-in-shopping-cart.jpg" alt="add enchiladas to your cart"/></a>
```
Bad (empty alt text and empty link text):
```html
<a href="/add-to-cart.html"><img src="enchiladas-in-shopping-cart.jpg" alt=""/></a>
```

### 4.10 Alt text generation checklist

Run in order, per `<img>`:

1. `alt` attribute present. *(H-62)*
2. If `alt=""`: image classified decorative **and** not the sole content of an `<a>`. *(H-70)*
3. Non-empty alt ≤ 2 sentences. *(H-63)*
4. Does not match `^(image|photo)\s+of\b`. *(H-64)*
5. First character uppercase; final character `.`/`?`/`!`. *(H-65)*
6. Not all caps. *(H-66)*
7. Token overlap with the adjacent paragraph below threshold. *(H-67)*
8. Identical source images across the corpus resolve to identical strings. *(H-68)*
9. No `longdesc` anywhere. *(H-69)*
10. Complex-image class (diagram, flowchart, graph, map, workflow GIF) → body-text long description required; if non-adjacent, alt names its location. *(§4.7)*
11. Alt does not begin with "The following diagram…" / "This screenshot shows…". *(H-71)*
12. Not a bare noun phrase; not an enumeration of colors and counts. *(§4.6)*
13. Generator received the surrounding paragraph as input. *(§4.4)*
14. Sampled for human review before publication. *(S-51)*

---

## §5 Motion, GIFs, and animation

### 5.1 The negative finding comes first

**The accessibility course contains essentially nothing on this topic (NEG-8).** An exhaustive inventory of everything motion-adjacent in the entire 31-page document:

- One embedded reference video: > "The following Google Chrome Developers video explores other examples of how context affects the way you describe an image: *Writing Good Alt Text - HTTP 203*."
- Nothing else.

Specifically **absent**: captions, transcripts, audio description, autoplay, pause/stop/hide controls, animation duration, flash thresholds (there is no three-flashes-per-second rule in the source), `prefers-reduced-motion`, and any GIF-specific guidance.

**Do not fabricate motion rules and attribute them to Google.**

### 5.2 What the sources *do* say that applies to a generated GIF

| Rule | Source | Wording |
|---|---|---|
| A GIF is an image, so it requires an `alt` attribute. | A11Y (H-62) | > "Every image requires an alt text element." |
| A GIF showing a multi-step process is a **complex image**: short alt plus a full textual description of the steps in the body text. | A11Y (§4.7) | > "For flowcharts and diagrams, explain the process or parts of your image in the text of your document." |
| GIF is an indexable image format, so animated GIFs are not an SEO liability. | SEO | > "Image formats: BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF" |
| Text visible only inside the animation is invisible to Google and to screen readers. | SEO | > "Googlebot can only find content that is textually visible. For example, text in videos is invisible to Googlebot." |
| Video pages: standalone page, near relevant text, descriptive title and description. | SEO | > "Create high-quality video content, and embed the video on a standalone page, near text that's relevant to that video." / > "Write descriptive text in the titles and description fields of a video (the title of a video is still a title, and so you can apply the best practices for writing titles here too)." |

**Operative rule for our GIF pipeline:** for every GIF that demonstrates a workflow, the body text must contain the equivalent numbered steps. The GIF is a supplement to the prose, never a substitute for it.

### 5.3 WCAG extension — clearly marked as not Google

**[EXTENSION]** The accessibility course cites WCAG as its authority for contrast, so citing WCAG for motion is consistent with its posture — but these are WCAG requirements, not quotations from any of the four courses. Attribute them to WCAG 2.2.

| WCAG SC | Requirement | Applied to our GIF pipeline |
|---|---|---|
| 2.2.2 Pause, Stop, Hide | Any motion that starts automatically, lasts more than 5 seconds, and is presented in parallel with other content must have a mechanism to pause, stop, or hide it. | An autoplaying looping GIF longer than 5 seconds is non-conformant unless the reader can stop it. Options: cap generated GIF duration at ≤ 5 seconds and do not loop; or ship a click-to-play poster frame; or ship `<video>` with controls instead of GIF. |
| 2.3.1 Three Flashes or Below Threshold | Nothing may flash more than three times per second. | Reject any generated GIF whose frame deltas produce >3 large luminance changes per second. Cursor blink and rapid UI transitions are the realistic risk. |
| 1.4.2 Audio Control | Auto-playing audio over 3 seconds needs a control. | Not applicable to GIF (no audio track). Applies if we ever emit `<video>`. |
| 2.3.3 Animation from Interactions | Motion animation triggered by interaction can be disabled unless essential. | Respect `prefers-reduced-motion` in the help center theme if GIFs are ever CSS-animated. |

---

## §6 SEO rules relevant to a hosted help center

Only rules that bear on writing and structuring documentation pages. See §6.6 for what was excluded.

### 6.1 Titles

| ID | Rule | Wording |
|---|---|---|
| SEO-1 | Give every page a descriptive, unique title. **HARD** | > "Make sure that every page has a descriptive title and meta description. Unique titles and meta descriptions help Google show how your pages are relevant to users, which in turn can increase your search traffic." |
| SEO-2 | A good title is unique, clear, concise, and accurate. | > "a good title is unique to the page, clear and concise, and accurately describes the contents of the page." |
| SEO-3 | Headings feed the title link, so headings matter to titles. | > "There are a few sources that Google uses to generate this title link, including the words inside the `<title>` element (also called the title text) and other headings on the page." |
| SEO-4 | The main heading must summarize the content and must not exaggerate. | > "Does the main heading or page title provide a descriptive, helpful summary of the content?" / > "Does the main heading or page title avoid exaggerating or being shocking in nature?" |

**NEG-6:** no title character limit exists in the source.

### 6.2 Meta descriptions and snippets

| ID | Rule | Wording |
|---|---|---|
| SEO-5 | Give every page a short, unique meta description covering the most relevant points. **HARD (presence, uniqueness)** | > "A good meta description is short, unique to one particular page, and includes the most relevant points of the page." |
| SEO-6 | Target one to two sentences (N14). **HARD** | > "the meta description tag, which is typically a succinct, one- or two-sentence summary of the page." |
| SEO-7 | Understand that the snippet usually comes from body copy, not the meta tag. | > "The snippet is sourced from the actual content of the page the search result is linking to, thus you have complete control over the words that can be used to generate the snippet. Occasionally the snippet may be sourced from the contents of the meta description tag." |

**Consequence:** the opening paragraph of a help article is doing snippet duty. Write it as a standalone answer.

Google's illustrated good snippet: *"Learn how to cook eggs with this complete guide in less than 5 minutes. We cover all the methods, including sunny side up, boiled, and poached."*

### 6.3 Headings and content organization

| ID | Rule | Wording |
|---|---|---|
| SEO-8 | Break long content into paragraphs and sections, and provide headings. | > "Break up long content into paragraphs and sections, and provide headings to help users navigate your pages." |
| SEO-9 | **Do not optimize heading order or count for Google.** This is an explicit non-rule and the one place SEO defers to accessibility. | > "Number and order of headings. Having your headings in semantic order is fantastic for screen readers, but from Google Search perspective, it doesn't matter if you're using them out of order. The web in general is not valid HTML, so Google Search can rarely depend on semantic meanings hidden in the HTML specification." |

### 6.4 Links, images, and URLs

| ID | Rule | Wording |
|---|---|---|
| SEO-10 | Anchor text: descriptive, reasonably concise, relevant to both pages. Merged into H-55/H-56/H-57. | > "Good anchor text is descriptive, reasonably concise, and relevant to the page that it's on and to the page it links to. It provides context for the link, and sets the expectation for your readers." |
| SEO-11 | Don't stuff keywords into anchor text. | > "resist the urge to cram every keyword that's related to the page that you're linking to… Ask yourself, does the reader need these keywords to understand the next page?" |
| SEO-12 | Link out to sources when it adds credibility. Use `nofollow` only for untrusted links; `sponsored` for paid; `ugc` for user-inserted. | > "using external links can help establish trustworthiness (for example, citing your sources)." / > "Use nofollow only when you don't trust the source, and not for every external link on your site." |
| SEO-13 | Place images near text relevant to the image. | > "Use images that are sharp and clear, and place them near text that's relevant to the image. The text that's near images can help Google better understand what the image is about and what it means in context to your page." |
| SEO-14 | Express key information in text, not only in graphics. | > "Put key information in text, not graphics, on the site." |
| SEO-15 | Use readable words in URLs; hyphens not underscores; no run-together words; no opaque or session IDs; normalize case; trim unnecessary parameters. | > "When possible, use readable words rather than long ID numbers in your URLs." / > "We recommend that you use hyphens (-) instead of underscores (_) in your URLs." Recommended: `https://example.com/summer-clothing/filter?color-profile=dark-grey`. Not recommended: `…/summer_clothing/…`, `…/greendress`, `…/2/6772756D707920636174`. |
| SEO-16 | Percent-encode non-ASCII as UTF-8. | Recommended: `https://example.com/gem%C3%BCse`. Not recommended: raw `https://example.com/gemüse`. |
| SEO-17 | Don't use URL fragments to change page content. Ordinary same-page heading anchors are fine. | > "Don't use fragments to change the content of a page, as Google generally doesn't support URL fragments. If you're using JavaScript to change content, use the History API instead." |
| SEO-18 | Image and video formats that are indexable. | > "Image formats: BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF" |

### 6.5 Canonicalization, moves, and content quality

| ID | Rule | Wording |
|---|---|---|
| SEO-19 | Each piece of content reachable at exactly one URL. | > "try to ensure that each piece of content on your site is only accessible through one individual URL" |
| SEO-20 | Consolidate duplicates by redirect first, `rel="canonical"` second. | > "try setting up a redirect from non-preferred URLs to a URL that best represents that information. If you can't redirect, use the rel="canonical" link element instead." |
| SEO-21 | Duplicate content is not a penalty — don't over-engineer around it. | > "If you have some content that's accessible under multiple URLs, it's fine; don't fret about it. It's inefficient, but it's not something that will cause a manual action. Copying *others'* content, however, is a different story." |
| SEO-22 | Permanent move → 301; temporary → 302; removed page → true 404, not a soft 404. | > "If you move a page permanently to another location, don't forget to implement 301 redirects for your page. If the move is only temporary for some reason, return 302." |
| SEO-23 | Multi-page articles need prominent, crawlable next/previous links. | > "be sure that there are prominent next and previous links for users to click (and that these are crawlable links)." |
| SEO-24 | Content must be original, complete, current, and free of spelling and grammatical mistakes. | > "The text is easy-to-read and well organized… free of spelling and grammatical mistakes." Review rubric questions: > "Does the content provide a substantial, complete, or comprehensive description of the topic?" / > "Does the content have any easily-verified factual errors?" / > "After reading your content, will someone leave feeling they've learned enough about a topic to help achieve their goal?" |
| SEO-25 | Anticipate the vocabulary of both novice and expert readers. | > "Users who know a lot about the topic might use different keywords in their search queries than someone who is new to the topic. For example, some users might search for 'charcuterie', while others might search for 'cheese board'." Caveat: > "don't worry if you don't anticipate every variation… Google's language matching systems are sophisticated." |
| SEO-26 | Don't keyword-stuff. | > "Excessively repeating the same words over and over (even in variations) is tiring for users, and keyword stuffing is against Google's spam policies." |
| SEO-27 | Don't let interstitials obstruct content. | > "advertisements, or interstitial pages… that make it difficult to use the website." For a help center this covers modal surveys, cookie walls, and upgrade interstitials over documentation. |
| SEO-28 | Attribute authorship where readers would expect it. | > "We strongly encourage adding accurate authorship information, such as bylines to content where readers might expect it." |

### 6.6 What was excluded as irrelevant

Read and deliberately dropped as out of scope for a hosted help center's authoring pipeline: crawling and indexing mechanics (Googlebot behavior, crawl-rate throttling, canonical-selection internals); `robots.txt` in all forms, `noindex`, password-protection as an indexing control; sitemaps; structured data and rich results in their entirety; JavaScript rendering and SPA/SEO concerns (only the authoring-facing fragment rule SEO-17 was kept); mobile-first indexing and mobile configuration; Core Web Vitals, PageSpeed, AMP, HTTPS migration; Search Console and analytics tooling; the entire "Promote your website" section; the entire "Do you need an SEO?" hiring page; whole-site migration, `hreflang`, and multi-regional/multilingual targeting (only single-URL 301/404 was kept as SEO-22, since help centers reorganize articles); crawl-budget management at the hundreds-of-millions-of-pages scale; all vertical business programs (Retail, Business Profile, News, Books, Scholar, YouTube, Merchant Center); and ranking-theory background (PageRank, meta keywords, subdomains vs subdirectories, TLD choice, quality-rater mechanics).

Also **absent rather than excluded**: the bundle references but does not contain the detailed `title-link`, `snippet`, and `google-images` pages. Any per-field character limits or filename conventions you might expect from those pages are simply not in the source (NEG-6, NEG-7).

---

## §7 Where accessibility and SEO overlap or conflict

**Governing principle: accessibility wins.** Justification is not merely ours — Google Search Central's own guidance on auto-generated "alternate texts for images" links to the accessibility course as the canonical spec, and SEO explicitly defers on heading semantics (SEO-9).

### 7.1 Agreements — implement once, satisfy both

| ID | Convergence | Evidence |
|---|---|---|
| O-1 | **Alt text is required on every image.** | A11Y: > "Every image requires an alt text element." SEO: alt "helps search engines understand what your image is about and the context of how your image relates to your page." A11Y names the SEO benefit itself: > "Descriptive alt text also helps to improve search results for images." |
| O-2 | **Alt text must be context-dependent.** | A11Y: > "Explain images in the context of the text." SEO: alt "explains the relationship between the image and your content," and images should sit > "near text that's relevant to the image." Both require the generator to see the surrounding prose. |
| O-3 | **Link text must be descriptive and self-sufficient.** The accessibility course calls out the overlap itself: > "Bonus: Informative link text also improves search engine optimization." | Merged blocklist: *Click here*, *Learn more*, *Read more*, *This document*, *website*, *article*, plus any empty anchor. SEO's out-of-context read test (H-56) is the mechanization of accessibility's "hear just the links" scan behavior — the same test, justified twice. |
| O-4 | **Plain, well-organized, short-sentence prose.** | A11Y wants active voice, short sentences, defined terms, lists over dense paragraphs for cognitive accessibility. SEO wants text "easy to follow," broken "into paragraphs and sections" with "headings to help users navigate." Same edits. |
| O-5 | **Don't lock information inside pictures.** | A11Y: text alternatives, complex images described in body text. SEO: > "Put key information in text, not graphics." Converges on one hard rule for a screenshot-heavy help center: **every screenshot must be accompanied by the equivalent instruction in prose.** |
| O-6 | **Headings are required structure.** | A11Y mandates real heading elements. SEO wants headings for navigation and uses them as a title-link source. No conflict on *having* headings. |

### 7.2 Divergences and their resolution

| ID | Tension | Resolution |
|---|---|---|
| **X-1** | **Heading semantics: mandatory (A11Y) vs. irrelevant (SEO).** A11Y: > "Don't skip levels of the heading hierarchy." SEO: > "from Google Search perspective, it doesn't matter if you're using them out of order." | **Not a real conflict — SEO is strictly permissive and endorses the accessibility rule** ("fantastic for screen readers"). Enforce H-53 and H-54 as HARD. There is no SEO cost. |
| **X-2** | **Link-text blocklist scope.** A11Y lists *Learn more*, *Click here*, *This document*. SEO's list is broader, adding *Read more*, *website*, *article*. | **Not a contradiction — a difference in coverage.** Take the union (H-55). Stated explicitly here so nobody later "corrects" the merged list back to one source. |
| **X-3** | **Empty alt: required for decorative images (A11Y) vs. a defect for linked images (SEO).** A11Y: use `alt=""` when decorative or duplicative. SEO labels `<a href="/add-to-cart.html"><img src="…" alt=""/></a>` as > "Bad (empty alt text and empty link text)" because > "Google uses the alt attribute of the img element as anchor text." | **This is the one real edge conflict, and it resolves by scope.** `alt=""` is permitted only for images that are (a) purely decorative **and** (b) not wrapped in, and not acting as, a link. `a > img:only-child[alt=""]` fails under both regimes — under accessibility because the link then has no accessible name, under SEO because it has no anchor text. Encoded as H-70. Secondary resolution, from accessibility's own guidance: > "Consider making a decorative image a CSS background image" — which removes the image from both the accessibility tree and the SEO surface. |
| **X-4** | **Alt-text length: A11Y caps it; SEO creates pressure to expand it.** Alt is an indexed signal and doubles as anchor text for image links, which tempts a generator toward keyword-loaded strings. | **Accessibility wins on length.** There is no SEO rule demanding longer alt text, and SEO explicitly forbids the failure mode: > "resist the urge to cram every keyword… keyword stuffing is a violation of our spam policies." Cap at 2 sentences (N11). If more detail is needed for discoverability, it belongs in the body text near the image (SEO-13/SEO-14) — which SEO says is where the context signal comes from anyway. |
| **X-5** | **"Don't duplicate surrounding text" (A11Y) vs. "place images near relevant text" (SEO).** | **Not a conflict — different fields.** The body text should be rich and adjacent (SEO-13); the alt string should be complementary rather than a copy (H-67). Require both. |
| **X-6** | **Color-based callouts: TW2 recommends them; A11Y forbids relying on color.** TW2: > "Adding a visual cue, for example, the red oval in the following figure, helps readers focus on the relevant section of the screenshot". A11Y: > "don't rely exclusively on the visual elements, such as the following: colors…" | **Genuine conflict between two Google courses. Resolved by house decision — see HOUSE-1 below.** |

### 7.1 House overrides

Decisions that intentionally depart from the source guidance. Recorded so they are visible and revisitable, not silently lost.

| ID | Override | Rationale and residual obligation |
|---|---|---|
| **HOUSE-1** | **Annotations use a single teal accent, `#01FEE0`, with a 3 CSS px stroke, across all screenshots, all products. Corners match the highlighted element: where the UI element has a corner radius (a button, pill, tab, card), the ring takes that radius plus its padding so it runs concentric with the control; where it has none (a row, a section, a group of controls), the ring uses the house 5 px.** Shape-and-label pairing (per X-6) is **not** required. | Decided 2026-08-18 (purple `#a855f7`, radius 14); **changed 2026-11-03** to teal `#01FEE0`, radius 5, then the same day to a 3 CSS px stroke (was 6) and corners matching the UI element (5 px fallback), at the GitKraken Desktop docs reviewer's request on gitkraken-desktop-docs#113 and the owner's decision to apply it to every product. Images captured before the change keep purple until they are next recaptured. Buys visual consistency across ~2,500 images and a much simpler annotation layer — one accent constant, no badge placement or numbering logic. **Residual obligation, which costs nothing extra:** because the system already generates alt text and prose for every annotated image, that text must name the control directly — "Click **Start Review**", never "Click the highlighted button" or "the teal box." Prose carries the meaning the color no longer has to. This satisfies Google's acceptance test — > "the text would be clear even if you removed all color and other visual indicators" — through the text channel rather than the visual one. |
| **X-7** | **Long-description pages (A11Y) vs. duplicate-content hygiene (SEO).** A11Y permits a complex image's long description to live > "on a separate page that you link to." SEO wants each piece of content at one URL. | **Not a conflict** — a long description is distinct content, not a duplicate. But an auto-generated description page needs its own title and meta description (SEO-1/SEO-5), a descriptive anchor (H-55), and its location named in the alt text if not adjacent (§4.7). |
| **X-8** | **Directional and color-based instructions: A11Y forbids them; SEO is silent.** | **Accessibility governs unopposed** (H-15). Incidental SEO benefit: the control's actual name is the term users search for (SEO-25). |
| **X-9** | **Automated generation: SEO adds governance that A11Y does not.** The accessibility course says nothing about who or what wrote the text. | Search Central does: auto-generated titles, meta descriptions, and alt text must meet > "accuracy, quality, and relevance" (S-51); scaled low-value generation risks a spam-policy violation (S-52); disclosure is encouraged > "where someone might think 'How was this created?'" (S-53). **For a system writing thousands of alt strings, this argues for a human review gate and sampling QA, not just a linter.** |
| **X-10** | **Anti-idiom rule provenance.** The accessibility course never uses the word "idiom" (NEG-10); TW1 does, at length. | **Resolved across sources.** H-9 is a TW1 rule. Cite TW1, not the accessibility course. |
| **X-11** | **Table rules.** TW1 supplies table *authoring* rules (N4, H-46, H-47). Neither the accessibility nor the SEO document supplies table *markup* rules (NEG-9). | Enforce the TW1 authoring rules. Do not invent `<th>`/`scope`/`<caption>` requirements and attribute them to these four courses; source them from WCAG or the Google developer documentation style guide and mark **[EXTENSION]**. |

---

## §8 Applying this to GitKraken help center content

### 8.1 The house context

| Property | Reality | Consequence |
|---|---|---|
| Format | Markdown with YAML frontmatter | Frontmatter fields are governed content, not metadata to ignore |
| Page title | Frontmatter `title:` — **the body contains no `# ` h1** (in `gitkraken-desktop-docs`, 90 markdown files contain 553 `##`, 557 `###`, and only 2 `# `) | H-52 is satisfied by the frontmatter, not by body markdown. **Never inject a `# ` heading into the body.** |
| Meta description | Frontmatter `description:` | This *is* the SEO-5/SEO-6 field. Enforce 1–2 sentences here. |
| Images | Raw `<img src='…' class="help-center-img img-bordered" alt="…">`, usually inside `<figure>` with `<figcaption>` | The rewriter edits the `alt=` attribute **in place**. Never convert to markdown `![]()` — markdown cannot carry the `class` attributes the theme depends on. |
| UI references | `<kbd>Preferences > General</kbd>` for controls; `**Application**` for tabs and options | This is the house equivalent of TW2's code-font rule (H-11), and it is the accessible-name carrier that makes H-15 satisfiable |
| Section dividers | `***` between sections | Rendered as `<hr>`. Semantic, decorative, no alt implications. |
| Products | GitKraken Desktop, GitLens, GitKraken CLI, GitKraken.dev, GitKraken Insights, GitKraken ADE, MCP Server, Git Integration for Jira — desktop, terminal **and** web applications (the full list is `src/core/registry.ts`) | Layout varies by platform and version |
| Audience | Developers and engineering managers | Assume Git fluency; do not assume GitKraken fluency |

### 8.2 Rules that need adaptation rather than literal application

| Google rule | Literal reading | GitKraken adaptation |
|---|---|---|
| **H-52** — "Use a level-1 heading for the page title" | Insert `# Title` at the top of every page | **Do not.** The platform renders the h1 from frontmatter `title`. Validate that `title` exists and is unique; treat the first body heading level (`##`) as the correct entry point. H-53 (no skipped levels) is then evaluated starting at `##`. |
| **H-27 / TW1 C3** — "Refactor amorphous adverbs and adjectives into objective numerical information" | Replace "much faster" with a percentage | **Flag only.** Google's own exemplar ("225-250% faster") supplies a number the source sentence did not contain. Per **H-79**, the rewriter flags the vague adjective and escalates; it never fabricates a benchmark, version number, keyboard shortcut, or menu path. |
| **H-3** — bold the expansion and the acronym on first use | `**Pull Request** (**PR**)` everywhere | Apply to **prose acronyms only**. Do not apply inside `<kbd>` UI labels or to product names already following house bolding, or the page becomes bold soup. |
| **S-36 / TW2 I7** — "the red oval" callout on screenshots | Draw a red oval | Use the standard teal accent (`#01FEE0`, 3 px stroke, the element's own corner radius or 5 px), uniformly, on every product. No shape or number pairing. Prose names the control. See **HOUSE-1** (§7.1). |
| **S-38 / TW2 I10** — export diagrams as SVG | Convert screenshots to SVG | Applies to **generated diagrams only**. Screenshots stay PNG; workflow demos stay GIF. All three are indexable (SEO-18). |
| **§4.3** — decorative images get `alt=""` | Use `alt=""` liberally | **Almost never applies here.** Every product screenshot is informative. Reserve `alt=""` for theme chrome. |
| **H-15** — no directional-only instructions | Delete directions | **Additive, not substitutive.** "Click <kbd>Activity Logs</kbd> in the footer toolbar" is compliant and better than either half alone. This matters more for us than for most docs because the same feature sits in different places in Desktop versus the web app. |
| **SEO-15/16/17** — URL structure | Restructure URLs | Advisory. Applies when articles are renamed or retired (SEO-22). **SEO-15's directory-threshold guidance (N15, "more than a few thousand URLs") does not apply at our corpus size** — do not reorganize on SEO grounds. |
| **S-54 / SEO** — don't fake freshness | — | Bump frontmatter `last_verified` **only** when content substantively changed. An automated rewrite pass that changes only wording is not a substantive change. |
| **H-72/H-73/H-75** — scope, non-scope, three-part introduction | Add new boilerplate sections | The house pattern already carries these: the opening "Use this page to…" paragraph is the scope statement, and the Requirements and limits section carries prerequisites. That section is a real heading (`## Requirements and limits`), never a bold line (H-51). **Enforce presence in the existing pattern; do not add a new "Scope" heading.** The gap to close is the *non-scope* sentence, which most pages lack. |
| **H-29** — conditions before instructions | Reorder every sentence | Maps cleanly onto our `os_support` / `hosted_variant` / `plan_required` frontmatter: platform and plan conditions belong in the Requirements and limits section **before** the Quick Start steps, and inline as "If you're on Windows, …". |

### 8.3 Alt text at GitKraken — current state and target

Measured across the docs repos:

| Repo | `<img>` tags | GIFs | Missing `alt` attribute |
|---|---|---|---|
| `gitkraken-desktop-docs` | 469 | 39 | 1 |
| `gitlens-docs` | 475 | 59 | 334 |
| `gitkraken-client-docs` | 665 | 80 | 665 |
| `git-integration-for-jira-cloud-docs` | 480 | 0 | 462 |

**The single highest-value fix in the entire corpus is H-62: emit an `alt` attribute on every `<img>`.** Roughly 1,460 of ~2,090 images currently have no `alt` attribute at all, which means screen readers announce filenames like `create-file-command-palette-2025.png`.

Alt length in the one repo that is already populated (`gitkraken-desktop-docs`, n=558): median 12 words, p90 22 words, max 43 words. For calibration, Google's rejected "too wordy" waffles example is 27 words. So roughly the top decile of our existing alt text is already past Google's informal line.

**Binding guidance:** the only Google-attributable limit is ≤ 2 sentences (N11, NEG-2). Any word cap we adopt is **[EXTENSION]** and must be labelled as ours. A working target of 10–20 words for a single-panel screenshot is consistent with Google's "just right" examples (7–14 words) without being falsely attributed to them.

**House alt-text pattern for product screenshots**, derived from §4.4 and §4.6:

- State what the reader is looking at and what it demonstrates, in the context of the step it illustrates.
- Name the product and the UI surface when the surrounding prose does not already.
- Do not enumerate every visible column, icon, and color.
- Do not restate the `<figcaption>` — the caption and the alt text are two different fields serving two different readers (H-67, S-32). Existing pages already do this correctly; preserve the distinction.
- For a GIF demonstrating a workflow, write a short alt describing the workflow and ensure the numbered steps appear in the body prose (§5.2).

### 8.4 Audience calibration (S-25 through S-29)

Applying the documentation equation to developers and engineering managers:

- **Assume:** Git fundamentals — commit, branch, merge, rebase, remote, stash, pull request. Do not re-explain these; doing so violates S-25 by supplying knowledge the audience already has.
- **Do not assume:** GitKraken product vocabulary — Launchpad, Workspaces, Cloud Patches, Focus View, the Commit Graph's specific affordances, plan-tier names. These are the terms that trigger H-1 and S-3.
- **Do not assume:** cross-product transfer. A GitLens reader is not necessarily a GitKraken Desktop reader. Per S-26, proximity differs even within one role.
- **Engineering managers** are a second role with different proximity: they read for capability and policy (plan tiers, SSO, admin controls, SOC 2), not for keystrokes. Pages tagged `audience: buyer` should not be rewritten toward the developer register.
- **S-28 applies at the product boundary:** an abbreviation that is obvious inside one product's docs may not be obvious in another's.

### 8.5 Governance for this system (X-9, S-51 through S-53)

1. **Human review gate on generated alt text.** Sample and review before publication. Google's standard for auto-generated alt text is > "accuracy, quality, and relevance."
2. **Never generate a page wholesale.** S-52 warns that > "using generative AI tools or other similar tools to generate many pages without adding value for users may violate Google's spam policy on scaled content abuse." Rewriting existing, human-authored pages is in scope; mass-generating new pages is not.
3. **H-79 is absolute.** No rewrite may introduce a factual claim absent from the source page.
4. **Preserve provenance.** Every automated change should be attributable in version control so a reviewer can distinguish a wording change from a factual change.

---

## §9 GitKraken writing rubric (house writing rules)

**Provenance.** GitKraken's writing rubric (16 files), its *10 major AI giveaways* checklist and its
product naming conventions, from the internal `gitkraken/gitkraken-marketing-os` repository
(`writing-rubric/`, `Misc/10 major AI giveaways.txt`, `brand/naming-conventions.md`). The rules are
restated here so the system needs no checkout of that repo. `standards/marketing-os-sync.json`
records the commit they were taken from; `npm run style` lists what has changed there since (§9.6).

**How it fits with §1–§8.** The Google courses (§2–§8) govern technical-documentation form:
structure, headings, accessibility, alt text, SEO. This section governs *how GitKraken writes*:
voice, word choice and the traps the rubric names. Both apply to every page. Where they pull apart,
clarity for the reader wins (precedence 1), then the house rulings in §9.4.

`R-n` rules are judgment rules (like §3): the prose writer applies them and the editorial pass
(§9.7) checks them. Where part of a rule is mechanically checkable, the lint rule is named.

### 9.1 Reader and purpose

| ID | Rule |
|---|---|
| R-1 | Clarity is measured in the reader's understanding, in context. Write for a known reader and their task: *When [situation], I need [task], so I can [goal].* |
| R-2 | Keep one clear aim per page and section. Decide coverage (how wide) and detail (how deep) for the reader, not for completeness. |
| R-3 | Write for people, not search engines. Length follows what the reader needs; every word costs them time. |
| R-4 | Relate new things to what the reader already knows. For a complete unknown, give the frame of reference first. |
| R-5 | Guard against *nerdview* (the curse of knowledge): no internal or code names, no implementation detail the reader cannot see or use. The scope rule that follows from it is HOUSE-7. **Lint: H-90, H-95, H-96.** |

### 9.2 Structure, titles, paragraphs

| ID | Rule |
|---|---|
| R-6 | Inverted pyramid: what the reader must know first, then explanation, then examples. Structures are tools, not templates. |
| R-7 | Use numbered steps for anything the reader does; use Q&A or problem/solution only when the subject calls for it. If two reader groups need different depth, give them different sections or pages. |
| R-8 | Titles and headings describe the content or the task (descriptive, *How to…*, or *-ing* forms). They never over-promise. |
| R-9 | One idea per paragraph: topic sentence, support, close. Short paragraphs. Use signposts (*Next*, *For example*, *However*) to link sentences. |
| R-10 | Write about the reader's work, not about the document or the app's internal layout. No narration of the docs ("this page covers", "these docs follow…", "as described above"), and describe UI layout only when a step needs it to find something. **Lint: H-91.** |

### 9.3 Sentences and words

| ID | Rule |
|---|---|
| R-11 | Basic sentences (subject, verb, object) for most points; vary rhythm; end on the significant word. Active voice. Say what *is*, not what is not. |
| R-12 | Talk to the reader: *you*, present tense, everyday speech, adult to adult, one consistent tone. |
| R-13 | Plain language: shorter, familiar, concrete, unambiguous words. Name who does what to which thing. Have the courage to be simple. |
| R-14 | Writing traps. Cut **padding** (*in order to* → *to*, *due to the fact that* → *because*, *in the event that* → *if*, *the majority of* → *most*, *at the present time* → *now*, *for the purpose of* → *to*, *by means of* → *with*); avoid needless **nominalisations**, **commercialese** (*leverage*, *seamless*, *proactively*) and **officialese** (*utilize* → *use*, *prior to* → *before*, *commence* → *start*, *terminate* → *end*, *ascertain* → *find out*, *endeavor* → *try*, *obtain* → *get*, *assist* → *help*, *ensure* → *make sure*). **Lint: H-92.** |
| R-15 | No **weasel words**: *up to*, *as many as*, *many*, *most*, *seems*, *probably*, *usually*, *quite*, *relatively*, *helps to* — give the number, the condition or the source instead. |
| R-16 | Metaphors only when they clarify; never in instructions. |
| R-17 | **AI giveaways** — none of: puffery (editorializing ordinary facts); giveaway vocabulary (*delve*, *tapestry*, *intricate*, *underscore*, *seamless*, *robust*); fake balance (*not just X, it's also Y*); trailing *-ing* commentary (*…, underscoring its role as…*); reflexive groups of three; fancy verbs for simple ones (*serves as* → *is*, *features* → *has*); em-dash overuse; mixed curly and straight quotes. **Lint: H-94** (vocabulary and phrases). |

### 9.4 House rulings (decided 2026-10-30)

| ID | Ruling | Why |
|---|---|---|
| HOUSE-2 | **No negative contractions in prose** (*cannot*, *do not*, *is not*). Positive contractions may stay where natural; instructions prefer the full form. Quoted UI strings stay exactly as the app shows them. **Lint: H-93.** | The rubric's accessible-language rule: negative contractions are misread. The Google courses are silent. (Help-center *narration* in GK-HC-Vids keeps contractions on purpose; that exception is for speech only.) |
| HOUSE-3 | **Numerals for numbers** (*3 tasks*), except at the start of a sentence and in quoted UI text. A sentence or list item never opens with a numeral: spell it out (*Two limits apply*) or reword (*You can run 3 tasks*). **Lint: H-97.** | Rubric: easier to scan. Google is silent. |
| HOUSE-4 | **UI names come from the product's own strings**, never from its code. Each product declares the internal terms that must not reach a page, with the UI name to use, in `src/core/registry.ts` (`internalTerms`). | R-5. Kepler's `rail` (the UI says *context panel*) reached 6 pages before this was enforced. |
| HOUSE-5 | **US English spelling** (*color*, *canceled*, *labeled*, *gray*). Quoted UI text stays as the product spells it. | One spelling per corpus; the products' UIs are US English. |
| HOUSE-6 | **Name things the way users see them** (decided by the owner 2026-10-30). In help-center pages, a control's, object's or feature's name and capitalization come from what the product's UI shows, not from marketing copy or code. Kepler: *task* in lowercase (New task, Tasks in progress), though `naming-conventions` capitalizes *Task* for marketing copy; the composer that starts a task is *the **New task** composer* (the UI never says "Task Composer"); the branch button on a task row is *the worktree button* (its label is *Worktree actions for {branch}*; "worktree pill" is a code name). Names the UI itself capitalizes (Agent Graph, Actions) stay capitalized. Where the UI shows no name at all, describe the thing by what the reader sees, and use that phrase consistently. | The docs describe the app the reader is looking at. A name or capital the screen never shows reads as a different thing, and a reader can't search the UI for it. |
| HOUSE-7 | **Document only what users can see, do or affect** (decided by the owner 2026-11-02). A help-center page describes the product as its user meets it: controls, labels, messages, settings, commands the user types, files the user edits, limits the user can notice, and the outcome of each. It does not describe how the product works inside. Test every section and sentence: *can a user see this, do this, or be affected by it in the product?* If not, it is cut; if it explains something visible, it is rewritten as that visible outcome. Out of scope, however accurate: internal routes, anchors and ids; link forms, URL parameters and syntax no UI produces or shows; source paths and component names; launch flags and arguments the product passes for you; timers, intervals, retry and backoff numbers; caches, storage, data models and fallback order; matching, resolution and sync algorithms; protocol names; design rationale ("that is why it is a radio control"); legacy keys kept for compatibility; changelog history. A change with no user surface gets the finding verdict `nothing`, and an empty docs search is a gap only when there is something a user can reach. Each product lists its internal-only syntax in `src/core/registry.ts` (`internalPatterns`). **Lint: H-95, H-96. Gates: `--user-surface` on actionable findings; `--scope` on the editorial pass.** | The Kepler v0.16 audit documented settings hash routes, `kepler://settings/<id>` links and `@id:` search because the diff added them and the docs had none; no user can create, copy or see any of them. A full read then found the same class of content (much of it older, written from the source) on 20 of 29 pages: Kepler-Docs #48. Accurate internals still cost the reader time and read as the product's own documentation of itself. |

### 9.5 Names

| ID | Rule |
|---|---|
| R-18 | Product names in full: **GitKraken Desktop** (never *GitKraken* or *Desktop* alone for the app), **GitLens** (one word, capital G and L), **Kepler**, **GitKraken Insights** (*Insights* on second mention), **GitKraken AI**, **GitKraken MCP**. *GitKraken* alone means the company or the platform. Spell out *agentic development environment (ADE)* on first use of *ADE*. |
| R-19 | Capitalize named features the way the product pages do (Commit Graph, Launchpad, Task, Action, Agent Graph). Generic Git terms stay lowercase mid-sentence (branch, commit, worktree, remote environment, skill). Plan names are proper nouns (Community, Pro, Advanced, Business). |
| R-20 | Partner names the way the vendor writes them: Claude Code, Codex, GitHub Copilot (*Copilot* after first mention), Cursor, OpenCode, Auggie. |

### 9.6 Keeping in step with the source

`standards/marketing-os-sync.json` records the `gitkraken-marketing-os` commit this section was last
brought up to date with, and the paths that matter.

```bash
npm run style                  # marketing-os commits touching those paths since the sync point
npm run style -- --stat        # + the files each commit changed
npm run style -- --mark        # after porting: record the commit you ported from (default HEAD)
```

It needs a `gitkraken-marketing-os` checkout beside this repo (or `GKDOCS_STYLE_REPO=<path>`), fetched
first; the script only reads. When a listed commit changes a rule, port it into §9 (and the lint
rules it names), run `npm test`, then `--mark` and commit both files. GK-HC-Vids keeps its own
sync point for the same sources (`docs/brand-sync.json`); the two move independently.

### 9.7 The editorial pass (required before `run --apply`)

Lint checks the mechanical subset. The judgment rules (§3 and §9) need a reader. Every page an audit
edits gets an editorial pass after its prose is written and before `run --apply`:

1. An editor (agent or person) who did not write the prose reads the **whole page** against §3 and
   §9 and edits it in place. No new facts and no lost facts (H-79), with one exception: content
   that fails the scope rule (HOUSE-7) is cut, or rewritten as the outcome the user sees. UI labels
   exactly as the product shows them; figures untouched except alt text or captions that break a
   rule (those images are then re-judged).
2. **Scope first.** Before style, the editor applies HOUSE-7 to every section of the page, including
   text that predates the audit: can a user see this, do this, or be affected by it?
3. **Humanizer last (added 2026-11-17).** After the style edits, the editor runs
   gitkraken-marketing-os's `ai-copy-humanizer` skill (`.agents/skills/ai-copy-humanizer/SKILL.md`)
   on the text the audit changed, reading its checklist live from `Misc/10 major AI giveaways.txt`
   (never from memory), in minimal-edit mode: fix real hits only, keep the voice. Where the skill and
   this file differ, this file wins for help-center pages (no negative contractions, UI labels
   verbatim, no new facts). Release-notes pages are exempt. It runs inside the pass, not after it,
   so its edits are in the bytes the record binds. The checklist's source is tracked by §9.6.
4. `gkdocs lint <page>` reports 0 errors, and no H-90 to H-97 warnings the editor could fix.
5. The editor records the pass: `gkdocs style review <product> <page> --reason "<what was checked
   and changed>" --scope "<what was confirmed user-facing, and what was cut>" --humanizer "<checklist
   items fixed (by number), or 'no checklist hits', and any hit left on purpose>"`. The record is
   bound to the page's sha256, so any later edit to the page voids it; a record without `--scope`
   (from before 2026-11-02) or without `--humanizer` (from before 2026-11-17) no longer clears the gate.

`run --apply` refuses while any page that a prose record names has no current, scoped, humanized style review —
the same way it refuses an unvalidated capture. The brief editors work from is
`standards/EDITORIAL-PASS.md`.

Outside an audit the pass is the same and as strict; only the record differs: `gkdocs style review
<product> <page-file> --standalone` and `gkdocs check <page-file>`, which no audit reads (CLAUDE.md
"Standalone checks", added 2026-11-18). `PAGE-RULES.md` and `IMAGE-STANDARDS.md` gather the other
rules a page change must meet, inside or outside an audit.
