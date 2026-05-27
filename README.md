# SBML Intern Claude Code Training

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sbml-lab/intern-claude-training)

> The Codespace will install all required tools automatically (bowtie2, samtools, MEME, Biopython, Claude Code CLI). First launch takes ~5 minutes.
>
> You will need to authenticate Claude Code with a **Pro plan** account after launch: run `claude` in the terminal.

## Overview

A 6-week training curriculum teaching interns how to use Claude Code to accelerate bioinformatics work in the SBML Lab (KAIST GSEB).

This training **runs alongside** the lab's existing 9-session bioinformatics curriculum — it does not replace it. Each module pairs with specific existing sessions.

## Curriculum

| Module | Topic | Paired with |
|--------|-------|-------------|
| 1 | What is Claude Code | Sessions 1–2 |
| 2 | GFF parsing + pandas with Claude Code | Sessions 3–5 |
| 3 | NGS alignment pipeline with Claude Code | Sessions 6–7 |
| 4 | Papers, MEME, and Biopython with Claude Code | Sessions 8–9 |
| 5–6 | Independent mini-project | — |

## Standing Rules

All interns follow these rules throughout the training:

1. `/log` at the end of every session
2. `/debug` before asking for help when something breaks
3. `/explain [concept]` before Googling
4. Plan mode (Shift+Tab) before writing any pipeline

## Included Skills

Three skills are included in this repo:

| Skill | Description |
|-------|-------------|
| `/log` | Record a session log entry — what you did, what broke, what you learned |
| `/debug` | Structured root-cause debugging before escalating for help |
| `/explain` | Get an explanation of a concept anchored to the lab's context |

## Prerequisites

- Claude Code Pro plan account
- Basic Python (covered in Sessions 1–5)
- Familiarity with the terminal

## Repository Structure

```
.claude/skills/         ← /log, /debug, /explain
.devcontainer/          ← Codespace configuration
lab-context.md          ← lab context for Claude Code
module1–module4/        ← training notebooks
module5-6-miniproject/  ← independent project template
instructor/             ← rubric and solutions
```
