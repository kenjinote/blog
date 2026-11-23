# Batch 080 source notes — Go installation and first program

Reviewed on 2026-11-23. The original Japanese edition and all twelve complete translations were read. Original publication date is 2022-09-10: `git log --follow` shows the 2022 source; a later SEO/date-injection commit added a conflicting 2026 date, which was removed. The URL slugs were left unchanged.

## Findings and corrections

- The prior article claimed Go does not use pointers. The Go FAQ discusses pointer values and explicitly explains why Go has no pointer arithmetic. Revised all editions to state both facts accurately.
- Replaced old installer screenshots and the legacy `go.shibu.jp` destination with the official OS/architecture-specific installation guide. Added `go version` as the installation check, and current official links for the getting-started tutorial, managing Go installations, FAQ, and Playground.
- The old one-file example used `go run hello.go` and implied every build produced `hello.exe`. Replaced it with the current module workflow in the official tutorial (`go mod init example/hello`, `go run .`), used `fmt.Println`, and clarified that executable naming/extensions depend on the OS.
- Kept the original publication date and set `lastmod: 2026-11-23` in all thirteen editions. Removed duplicate injected dates.

## Primary sources

- https://go.dev/doc/install
- https://go.dev/doc/tutorial/getting-started
- https://go.dev/doc/manage-install
- https://go.dev/doc/faq
- https://go.dev/play/

## Limits

Review is AI-only. No native-speaker review or installation on each operating system/CPU architecture was performed. The local environment has no Go toolchain, so the sample was checked against the official tutorial and equivalent static checks; it was not executed locally. The public CI/Hugo and post-deployment checks remain pending.
