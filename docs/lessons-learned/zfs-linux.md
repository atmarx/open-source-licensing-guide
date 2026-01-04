# ZFS on Linux: A Compatibility Tragedy

**Lesson:** License incompatibility has real costs

## The Setup

ZFS is arguably the most advanced filesystem ever created. Developed by Sun Microsystems, it offers features that Linux filesystems still lack: integrated volume management, snapshots, checksumming, self-healing, and more.

Linux is the dominant server operating system. Millions of servers, countless applications, the foundation of cloud computing.

You'd think they'd go together. They don't—or at least, not cleanly.

## The Problem

ZFS is licensed under CDDL (Common Development and Distribution License). Linux is licensed under GPL v2.

CDDL and GPL are both copyleft licenses. Both require derivative works to use the same license. When you combine CDDL code and GPL code, both licenses claim the result—and they can't both be satisfied simultaneously.

The Free Software Foundation considers them incompatible.[^zfs-issues] So does the Linux kernel project.

## The Consequences

### No native ZFS in Linux

The Linux kernel cannot include ZFS directly. The license conflict prevents it.

This means:

- No ZFS support out of the box
- Third-party modules required
- Potential instability from out-of-tree code
- Complications for distributions

### The Workaround

OpenZFS exists as a kernel module that users can install separately. It works—millions of people use ZFS on Linux successfully. But:

- It's not in the mainline kernel
- Every kernel update risks breakage
- Some distributions won't include it
- Legal uncertainty persists

Ubuntu includes ZFS despite the licensing concerns, arguing their interpretation allows it. Fedora and Debian have been more cautious.

### Canonical's Position

Canonical (Ubuntu's parent company) argues that kernel modules loaded at runtime are not "derivative works" of the kernel, so the GPL's copyleft doesn't apply to ZFS. This interpretation is... contested.

No court has ruled on it. The Linux kernel developers generally disagree with Canonical's interpretation. Users are caught in the middle.

## Why This Happened

### Sun's choice

Sun chose CDDL partly to prevent their code from being absorbed into Linux without contributing to Solaris (Sun's operating system). It was a strategic decision, not an accident.

When Oracle acquired Sun, they could have relicensed ZFS under GPL. They chose not to.

### The GPL v2 limitation

Linux uses GPL v2 specifically, not "GPL v2 or later." GPL v3 addressed some compatibility issues, but Linux can't adopt v3 without re-licensing the entire kernel—an impossible task given the number of contributors.

This wasn't foreseeable when Linus chose GPL v2 in 1991, but it's a constraint now.

## The Lessons

### License incompatibility is real

This isn't theoretical. One of the best filesystems in existence cannot be properly included in the most important operating system because the licenses don't mesh.

Millions of users are affected. The engineering cost of workarounds is substantial. The legal uncertainty persists.

### Strategic licensing has consequences

Sun's choice to use CDDL achieved its goal: ZFS wasn't absorbed into Linux while Sun existed. But it also prevented ZFS from reaching its potential audience, and now that Sun is gone, the restriction serves no one's interests.

### Some damage is permanent

Even if Oracle relicensed ZFS tomorrow, the years of fragmentation and workarounds can't be undone. Trust and momentum, once lost, don't fully return.

## What This Means For You

When choosing a license:

- Consider what other projects you want compatibility with
- Copyleft licenses can conflict with each other
- Strategic restrictions may backfire long-term

When adopting dependencies:

- License compatibility matters for integration
- Check whether the licenses of your dependencies are compatible with each other
- "Both open source" doesn't mean "compatible"

ZFS on Linux works, technically. But it could have been so much simpler. The license friction is a tax that every user pays, indefinitely.

[^zfs-issues]: See [ZFS Linux Licensing Issues](../reference/sources.md#zfs-linux-licensing-issues)
