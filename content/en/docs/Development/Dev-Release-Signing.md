---
title: "Release Signing"
linkTitle: "Release Signing"
weight: 60
description:
  "Information on how SW360 deliverables are signed and how to verify them."
---

# Release Signing and Verification

To ensure the integrity and authenticity of SW360 deliverables, we use
cryptographic signing for both our container images and source code tags.

## Container Image Signing (Cosign)

All Docker images published to the GitHub Container Registry (GHCR) are signed
using **Sigstore/Cosign** with keyless signing (OIDC). This process links the
image to the specific GitHub Action workflow that built it.

### How to Verify

1.  **Install Cosign**: Follow the [official installation
    guide](https://docs.sigstore.dev/cosign/system_config/installation/).
2.  **Verify an Image**: Use the following command to verify the signature of an
    SW360 image:

    ```bash
    cosign verify ghcr.io/eclipse-sw360/sw360 \
      --certificate-identity-regexp https://github.com/eclipse-sw360/sw360/.github/workflows/sw360_container.yml@refs/heads/main \
      --certificate-oidc-issuer https://token.actions.githubusercontent.com
    ```

    *Replace `ghcr.io/eclipse-sw360/sw360` with the specific image you wish to
    verify (e.g., `sw360/keycloak` or `sw360-frontend`).*

If the verification is successful, you will see a JSON output containing the
"Critical" statement and information about the signer.

## Git Tag Signing

Official releases of SW360 are marked with signed Git tags. Furthermore, the
project requires all commits to be cryptographically signed by contributors.
This ensures that the entire development history and the final release source
code have not been tampered with.

### How to Verify

1.  **Check Verification Status**: On GitHub, look for the **"Verified"** badge
    next to commits and tags.
2.  **Verify a Tag Locally**: Use the following command to verify a specific
    release tag:

    ```bash
    git tag -v <tag_name>
    ```

    If the tag is validly signed, Git will output a message starting with
    `gpg: Good signature from...`.
