---
title: Verifying an email signup end to end
description: The form returned success. The subscriber appeared in the right group. The one thing that failed was in an inbox I do not control.
date: 2026-10-08
lang: en
topic: ai-and-engineering
tags: [site-notes, sources-and-method]
---

This site has a signup form and a double opt-in. When you submit it, the mailing tool sends you a
confirmation email, and until you click the link in that email you are not on the list.

I wanted to know whether that actually worked, so I ran the loop once, with a real address, and
checked the state at each step. Here is what "checked" meant, and the failure that only showed up
at the far end.

## What the states look like

The tool has two states that matter: `Unconfirmed` and `Active`. A new signup lands in
`Unconfirmed`, does not appear in the default list of subscribers, and does not count towards the
group's size. That is correct behaviour for double opt-in, and it is also the single most
confusing thing about the setup: the list looks empty right after a successful signup.

So the check is not "did the count go up". It is a sequence:

1. Submit the form on the live site, from the live site's own page, and read the response. Mine
   came back `{"success": true}` and the page replaced the form with a thank-you message.
2. Open the subscriber record and read four fields: status `Unconfirmed`, the source line naming
   the form, the group it was added to, and the activity entry that says it was added.
3. Check the campaign report for the confirmation email and confirm its sent counter moved from 1
   to 2. The number matters: a signup that produces no outgoing mail is a broken loop that looks
   like a working one.
4. Wait for the recipient to click the link, then read the record again and watch the status move
   to `Active`, the group count move with it, and the unconfirmed count go back to zero.

Only after step 4 is the pipeline verified. Steps 1 to 3 prove the plumbing; step 4 proves the
part a reader actually performs.

## The thing that failed was the inbox

The confirmation email was sent. It never arrived.

The address in question was a QQ Mail account, and QQ Mail silently drops mail from foreign
senders. No bounce, no spam folder entry, nothing in the logs on my side. The mailing tool
reported a successful send, and it was telling the truth.

This is worth stating plainly because it is invisible from the sending side. Every dashboard I can
look at says the email left. The only way to learn otherwise is to ask the person at the other end,
and a signup flow that depends on them telling you is a signup flow that will lose readers without
ever showing an error. The practical fixes are ordinary ones: tell people which folder to check,
use a mailbox you trust for your own tests, and expect some fraction of a list to be unreachable
through no fault of your own.

## Two smaller traps

**The dashboard's copy was arguing with the site.** The embedded form ships with a default headline
and the line "Signup for news and special offers!", which is roughly the opposite of what this site
promises. The form editor is a client-rendered app, and synthetic clicks from a scripted browser
do not reach its text-editing state, so there was no clean programmatic fix. I hid those two
elements in CSS and let the site's own heading stand. That is a workaround and it is labelled as
one in the stylesheet.

**The status filter is not a native control.** Selecting "Unconfirmed" means clicking a custom
overlay, and clicking where the option was last time lands on nothing, because the menu re-renders.
What works: send an Escape first in case the menu is already open, click the trigger, re-read the
option's coordinates after it opens, and then click. The confirmation that the filter is applied is
a line of text reading which status is being shown, not the menu's own state.

## Cleaning up after yourself

The test created subscriber records in a real account, so the last step was deleting them, which is
also the step that is easy to skip. I kept two addresses deliberately, for future sends: the one
that can receive foreign mail and the one that cannot. Knowing which is which is useful the next
time a confirmation email "sends successfully".

## What I would still verify

Payment. The support page has a working button and a payment page that returns 200, and I have
never completed a real transaction through it. Until I do, the honest description of that button is
"untested", not "working". The same standard applies here: the signup was verified end to end
because a person on the other side clicked a link and the state changed. Anything less than that
is a hope with a green tick next to it.
