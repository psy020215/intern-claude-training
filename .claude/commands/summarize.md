---
name: summarize
description: Summarizes what happened in the current session (files edited, commands run, issues hit) into a 3-sentence recap for sharing with a supervisor.
---

# Session Summary

## Purpose

Summarize what happened in the current session so the user can see not only what was modified or executed, but also what problems occurred and what remains unresolved.

## Process

1. Review the conversation so far in this session — note which files changed, which commands or scripts ran, and what the user asked along the way.

2. Condense that into exactly 3 sentences, one for each of:
   - What got done this session
   - Any error, failure, or unexpected behavior that came up
   - Anything still pending or left unresolved

3. Output the 3 sentences straight to the terminal — don't write them to a file — so the user can paste them into a note or send to their supervisor.
