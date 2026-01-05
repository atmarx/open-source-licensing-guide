# MySQL and the MariaDB Fork

**Year:** 2009-2010

**Lesson:** Sometimes the community forks before anything goes wrong

## What Happened

MySQL was the world's most popular open source database. The "M" in LAMP stack. The backbone of countless web applications. Licensed under GPL with a commercial dual-licensing option.

Sun Microsystems acquired MySQL AB in 2008 for $1 billion. The community was cautiously optimistic—Sun had a decent open source track record.

Then Oracle announced it was acquiring Sun.

Oracle already owned a competing database. Oracle Database was their flagship product, the source of their enterprise dominance. Now they would own MySQL too.

The community didn't wait to see what would happen.

## The Preemptive Fork

Michael "Monty" Widenius, MySQL's original creator, forked the project in 2009—before Oracle's acquisition of Sun had even closed. He called it MariaDB (after his daughter, continuing the family naming tradition—MySQL was named after his other daughter, My).

!!! terminal inline end ""
    Most forks happen in panic. This one was strategic. Monty saw what was coming and moved before the crisis hit.

This was unprecedented. Previous forks happened in response to license changes or governance failures. MariaDB was forked in anticipation of problems that hadn't occurred yet.

Monty's stated concerns:

- Oracle had no incentive to develop MySQL when it competed with their core product
- Oracle's history with open source was... not encouraging
- The dual-licensing model gave Oracle control over MySQL's future
- Once Oracle owned it, forking would be harder (contributor agreements would flow to Oracle)

## Oracle's Stewardship

To be fair to Oracle: they didn't kill MySQL. They continued development. They released new versions. MySQL didn't die.

But the community's fears weren't entirely unfounded either:

- Development velocity slowed compared to the Sun era
- Some features appeared in Oracle's commercial MySQL Enterprise before the community edition
- Oracle sued Google over Java (a Sun acquisition), demonstrating willingness to litigate
- The relationship between Oracle and the open source community remained... tense

## The Distribution Response

Linux distributions started switching. One by one, major distributions replaced MySQL with MariaDB as the default:

- Fedora (2013)
- Red Hat Enterprise Linux (2013)
- Debian (2015)
- Ubuntu (optional, with MariaDB in repositories)

The reasoning varied, but the pattern was clear: distributions trusted MariaDB's governance more than Oracle's.

## MariaDB's Trajectory

MariaDB didn't just survive—it diverged. What started as a drop-in replacement developed its own features, its own storage engines, its own identity.

The MariaDB Foundation provides governance. Multiple companies contribute. No single entity controls the project's future.

This is exactly what Monty intended.

## The Lessons

### Preemptive forking works

The community didn't wait for Oracle to do something harmful. They created an alternative while MySQL was still healthy, making migration easy. By the time anyone needed to leave MySQL, MariaDB was mature and proven.

### Founder credibility matters

Monty wasn't a random developer forking a project. He created MySQL. When he said Oracle's ownership was concerning, people listened. His involvement gave MariaDB instant legitimacy.

### Dual licensing creates leverage

MySQL's dual-licensing model (GPL for open source use, commercial license for proprietary embedding) meant the copyright holder had significant control. Contributors signed agreements that gave MySQL AB—and later Oracle—special rights. This made the timing of the fork critical.

### Governance is a feature

MariaDB Foundation governance means no single company controls the project. Distributions chose MariaDB partly because of this structure. When evaluating dependencies, governance is as important as features.

## What This Means For You

When a major project is acquired:

- Watch for signs of slowing development
- Note whether the acquirer has competing products
- Check if a credible fork exists
- Consider migrating before you're forced to

When choosing database infrastructure:

- Governance structure affects long-term risk
- Drop-in compatibility makes migration possible—but only if you migrate before divergence
- Community health matters as much as feature lists

MySQL still exists. MariaDB thrives. Both outcomes were enabled by the GPL—Oracle couldn't close the source, only affect the direction. The license protected the code; the fork protected the community.

