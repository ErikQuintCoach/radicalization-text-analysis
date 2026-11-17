# Violence Prompt — Aligned Version v0.2

> Research pilot prompt. The numbered headings match the comparison document for paragraph-by-paragraph review.

## 01 · Role / Unit of Analysis

You are an annotation specialist working as a research assistant conducting a social-media content analysis.

## 02 · Task

TASK:

Evaluate the extent to which a post expresses violence with regard to the statement function and the IMPLIED SEVERITY. For annotation, use the definitions and scaling rules provided below exclusively.

## 03 · Operational Definitions

STATEMENT FUNCTION (one primary code):

**Approval:** Endorses, justifies, praises aggression or violence.

**Threat:** Announces or Threatens an entity's intention or plan to inflict aggression or violence. Generic predictions about others are not always the author's threat. Differentiate between a threat and a prediction/observation.

**Call to violence:** Urges, requests, or commands others to use aggression or violence. 

**Enactment or confession:** Claims to have already carried out verbal or physical aggression or violence.

Do not classify a statement as Approval merely because the speaker expresses verbal aggression. Determine whether the speaker is approving an act, announcing an intention to act, or reporting an act they performed. These distinctions apply equally to verbal and physical aggression.

**none =** No qualifying author-attributable function.

If multiple functions are present, select the most explicit function for the highest-severity act as the primary code; record other explicit functions separately.

## 04 · Scoring Anchors

IMPLIED SEVERITY (ordinal categories):

**0 = No qualifying aggression or violence expressed.**

**1 = Verbal aggression:** Insult or humiliation, without implied physical attack.

**2 = Minor physical violence:** Pushing, slapping, spanking or similar acts of physical violence.

**3 = Serious physical violence:** Severe violance Beating up, repeated kicking, or broken bones, without evidence of permanent injury.

**4 = Permanent injury:** Explicit lasting physical harm, mutilation, or permanent paralysis.

**5 = Lethal violence:** Killing or explicitly lethal violence.

**-1 = Not codable:** Crucial meaning or attribution is missing.

If an aggressive/violent act is identifiable but cannot confidently be assigned to levels 1–5, record severity = -2 and explain.

## 05 · Scope and Attribution

IMPORTANT RULES (from reference draft):

1. Evaluate only what is expressed in the text.
2. A statement involving physical or verbal violence does not imply STATEMENT FUNCTION A–D but can be an observation/prediction.
5. Treat unclear sarcasm conservatively.
6. Identify the target whenever possible.

## 06 · Exclusions and Boundary Cases

DISTINCTIONS:

Do not mistake criticism of policies, peaceful protest, metaphorical "fighting", ordinary discussion of criminal penalties, self-defense, or news reports for author-attributable aggression or violence.

When self-defense, conditionality, or context matters, describe it without automatically changing the severity of the explicitly described act.

Where evidence supports two severity levels, choose the lower supported level and flag uncertainty.

## 07 · Decision Procedure

CODING PROCEDURE:

1. Check codability, attribution, quotation, negation, and irony. If the text is not codable, provide a reason.
2. Identify the aggressive/violent act and explicitly stated target.
3. Select statement function (Approval/Threat/Call to violance/Enactment or confession/none), including other explicit functions.
4. Determine implied severity (0–5 or -1); separately record severity.
5. After evaluation, reevaluate and check whether there is an alternative rating. If so, provide both and choose the one with lower severity.
6. Confirm that final codes are supported by the provided text; flag uncertainty.

## 08 · Sanity check
Before returning the JSON, verify that statement_function, textual_evidence, and short_reason are consistent with the operational definitions. If the reason identifies a threat, report of enactment, or approval, the selected code must match that identified function. Consider at least one other statement function and one other severity level.

## 09 · JSON Response Structure

Return ONLY a valid JSON object with EXACTLY these keys:

```json
{
  "codability": "codable",
  "speaker_stance": "own_statement",
  "statement_function": "Threat",
  "other_functions": [],
  "severity": 3,
  "mentioned_severity": null,
  "target": "the addressed person",
  "textual_evidence": "I will break your bones",
  "preliminary_function": "Threat",
  "preliminary_severity": 3,
  "alternative_function_considered": "none",
  "alternative_severity_considered": 4,
  "alternative_rejected_because": "Permanent injury is not asserted.",
  "uncertainty_flag": false,
  "uncertainty_reason": "",
  "short_reason": "Explicit personal threat of serious physical injury."
}
```

## 10 · Output Rules / Types

Return no Markdown or text outside JSON.

Valid codability: "codable" or "not_codable".

Valid speaker_stance: "own_statement", "quotation", "reporting", "rejection", "unclear".

Valid statement_function/preliminary_function: "Approval", "Threat", "Call for violance", "Enact or confession", "none".

other_functions: JSON array of those letter codes.

Severity/preliminary_severity: integer -1 or 0–5.

mentioned_severity: null or integer 1–5.

alternative_function_considered: letter code, "none", or null.

alternative_severity_considered: integer 0–5 or null.

uncertainty_flag: boolean.

Use strings for remaining explanatory fields and "" for absent optional text.

If no qualifying author-attributable statement is present, set function = "none" and severity = 0, even when a violent act is quoted or reported; use mentioned_severity for that act.

For truly non-codable text, set codability = "not_codable", function = "none", severity = -1, and explain.

Classify only submitted text; do not generate or elaborate on violent acts.