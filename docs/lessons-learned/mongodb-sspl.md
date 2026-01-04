# MongoDB and the SSPL

**Year:** 2018
**Lesson:** The cloud provider problem has no clean solution

## What Happened

MongoDB was one of the great open source success stories. A document database that developers loved, licensed under AGPL, backed by a company that went public. The model seemed to work.

Then came the cloud providers.

AWS, Azure, and GCP began offering MongoDB as a managed service. They took the open source code, ran it at scale, and sold it as "Database as a Service." MongoDB Inc. built the software; cloud providers captured the value.

MongoDB's response: the Server Side Public License (SSPL).[^mongodb-sspl]

## The SSPL

SSPL is AGPL on steroids. Like AGPL, it requires source code disclosure when software is offered over a network. Unlike AGPL, the disclosure requirement extends to the *entire stack*:

> If you make the functionality of the Program or a modified version available to third parties as a service, you must make the Service Source Code available... "Service Source Code" means the Corresponding Source for the Program or the modified version, and the Corresponding Source for all programs that you use to make the Program or modified version available as a service, including... management software, user interfaces, application program interfaces, automation software, monitoring software, backup software, storage software and hosting software, all such that a user could run an instance of the service using the Service Source Code you make available.

In plain terms: if you offer MongoDB as a service, you must open source your entire cloud infrastructure.

## The Reaction

### OSI rejected SSPL

The Open Source Initiative reviewed SSPL and declined to approve it.[^sspl-not-open-source] They concluded it didn't meet the Open Source Definition—specifically, it discriminates against certain uses (running as a service) and creates practical barriers to compliance.

MongoDB is no longer open source by the accepted definition.

### Major distributions dropped it

Debian, Fedora, and Red Hat removed MongoDB from their repositories. SSPL wasn't acceptable under their guidelines.

### Cloud providers responded differently

AWS launched DocumentDB, a MongoDB-compatible database they built themselves. Azure and GCP eventually made licensing deals with MongoDB Inc.

The SSPL worked as intended: it forced cloud providers to either build their own implementation or pay MongoDB.

## The Debate

### The MongoDB perspective

> "We wrote the software. Cloud providers are free-riding on our work. If AGPL's network clause isn't enough to stop them, we need something stronger. Why should they profit from our engineering while contributing nothing back?"

### The open source purist perspective

> "You chose open source. You benefited from community contributions. Now that cloud providers can play by the same rules you did, you're changing those rules. SSPL isn't open source—it's source-available with restrictions."

### The pragmatic perspective

> "MongoDB needed to survive. Their business model was under threat. Whether SSPL is 'open source' or not, it was a rational business decision."

## The Lessons

### The cloud provider problem is real

Building a sustainable business on open source infrastructure software is genuinely hard. Cloud providers have advantages—scale, existing customer relationships, trust—that open source companies can't easily match.

### Relicensing breaks trust

The community that built MongoDB under AGPL didn't sign up for SSPL. Their contributions are now under a license they never agreed to. This erodes trust in open source projects backed by single companies.

### "Open source" has a definition

MongoDB can call SSPL whatever they want. The OSI, Debian, Fedora, and Red Hat call it "not open source." Words matter. Definitions matter.

### The problem isn't solved

SSPL didn't fix MongoDB's cloud provider problem—it just changed the negotiating dynamics. The fundamental tension between open source sustainability and cloud economics remains.

## What Came After

MongoDB's SSPL was the first major "source available but not open source" response to cloud providers. It wasn't the last. Elastic, Redis, and others followed with their own restrictive licenses.

The pattern is now established:

1. Company builds successful open source infrastructure
2. Cloud providers offer it as a service
3. Company changes license to restrict cloud providers
4. Community forks or moves on
5. Repeat

Whether this is tragedy or adaptation depends on your perspective.

[^mongodb-sspl]: See [MongoDB SSPL License Change](../reference/sources.md#mongodb-sspl-license-change)
[^sspl-not-open-source]: See [SSPL Open Source Initiative Rejection](../reference/sources.md#sspl-open-source-initiative-rejection)
