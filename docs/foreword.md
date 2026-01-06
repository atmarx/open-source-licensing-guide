# Foreword

## About the Voice

If you've read any of the pages on this site already, you've met the narrator—[a grizzled veteran who watched the free software movement unfold](./preface.md) from the beginning. That voice is a deliberate choice.

I wanted this guide to feel like getting advice from someone who'd seen it all. Not a legal textbook, not a Wikipedia article, but the kind of practical wisdom you'd get from a mentor who's been around long enough to know where the bodies are buried. The voice is a composite—part oral history, part active participant in the madness, and part "the tone I wish someone had used when explaining this stuff to me".

The events are real. The lessons are real. The "*I was there*" framing is a narrative device. Consider it historical fiction in service of education.

## About Me

My name's Andrew, and I was born in 1983—the same year Richard Stallman announced [the GNU Project](https://www.gnu.org/). My dad brought home an [IBM PC AT](https://en.wikipedia.org/wiki/IBM_Personal_Computer_AT) when I was five, and I've been fixing, using, and explaining computers ever since.

I grew up in the middle of it. My dad replaced the AT with a 386DX-33 and I got my first taste of Windows 3 after years of only DOS. We finally retired the dot matrix printer that had buzzed through my childhood (including the first printed report my 1st grade teacher had ever received from a pupil), replacing it with a slick laser that could spit out *multiple* pages a minute. I read [*Where Wizards Stay Up Late*](https://www.simonandschuster.com/books/Where-Wizards-Stay-Up-Late/Katie-Hafner/9780684832678) and wanted to start my own ISP. I was my high school's webmaster while the browser wars raged (*"it's fine in Navigator, but why does it look so weird in IE4?"*).

But I was young. I watched the foundational battles from the sidelines—seeing the names and players connected to software I used, but lacking the political understanding to connect the bigger picture. I heard the names—[Stallman](https://en.wikipedia.org/wiki/Richard_Stallman), [Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), [Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond)—but I knew them the way a kid knows the adults are discussing something important without quite grasping what.

## Why This Guide Exists

I now work with researchers and developers, many of whom are even further removed from this history than I am. "Open source" is just *how software works now*. Most have never had to think about why [MIT](./licenses/permissive/mit.md) and [GPL](./licenses/copyleft/gpl.md) are different, or what it means when a company relicenses their project. They assume someone else has figured this out[^overhead].

Someone has[^myjob]. But that knowledge lives in mailing list archives, conference talks, and the memories of people who were there. It's not written down in one place, in plain language, for people who just need to understand enough to make good decisions.

This guide is my attempt to fix that, and to learn something along the way.

## How This Was Made

I built this guide with Claude, Anthropic's AI assistant. Claude helped me research, organize, write, and maintain something resembling academic rigor.

The collaboration worked like this: I knew what I wanted to say and roughly how I wanted to say it. Claude helped me say it clearly, consistently, and with proper citations. Every claim is sourced, and every opinion is marked as opinion. The errors that remain are mine.

Using AI to write about open source licensing feels appropriate, somehow, given how much of the software used to build the LLMs rely on these very same licenses. Similar to what the theory of linguistic relativity says about language defining the bounds of our possible worldviews, the tools we use to create and develop shape *how* we work.  My use of AI has allowed this project to be far more complete and complex than I could have otherwise accomplished. Acknowledging this use is critical as we find ourselves surrounded by more and more "AI slop"--which I hope this guide is not just another example of!

## Companion Guide

This guide has a sibling: [The Weight of Your Dependencies](https://build.xram.net), which covers the practical side of building software responsibly—dependency management, supply chain security, and what happens when the code you rely on changes out from under you. If licensing tells you what you *can* do with code, that guide helps you think about what you *should* do.

## License

This guide is released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)—Creative Commons Attribution-NonCommercial 4.0 International.

You're free to share and adapt this material for non-commercial purposes, as long as you give appropriate credit. If you're an educator, researcher, or developer trying to understand licensing better, this is for you. If you're a company that wants to use this for training materials, let's talk.

Why NonCommercial? Because I built this to help people, not to create a product. The NC clause keeps it that way while still allowing the sharing and adaptation that makes open resources valuable.

---

*— Andrew Marx, 2026 @ [github.com/atmarx/open-source-licensing-guide](https://github.com/atmarx)*

[^overhead]: "That's what overhead is for!" they shout in unison.
[^myjob]: "I know.  It's literally my job." I reply with a wink.