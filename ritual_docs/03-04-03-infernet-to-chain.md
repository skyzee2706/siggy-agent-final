> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Infernet ↔︎ Chain

> Ritual, with its underlying mesh of 8,000+ connected Infernet nodes, lets anyone, anywhere tap into transparent AI, with strong privacy and verifiability guardrails.

<Frame>
  <video src="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/videos/infernet-and-chain.mp4?fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=fee14be8caf1cb39aa45cec4ae5e6dec" autoPlay controls disablePictureInPicture loop playsInline muted preload="auto" data-path="assets/videos/infernet-and-chain.mp4" />
</Frame>

## Background

### Centralized APIs are broken

Access to AI inference is dominated by a handful of centralized operators
serving models via API. These service providers
[geo-restrict access](https://techcrunch.com/2023/04/01/chatgpt-blocked-in-italy/),
require operator trust, and censor.

Developer experience using these APIs is cumbersome, with limited optionality.
Because of closed-source moats, these centralized model providers unilaterally
price and serve compute, without any competitive market mechanism to drive cost
savings for developers or end-users.

<Card title="Crypto × AI" icon="link" img="/assets/images/crypto-x-ai.svg" href="/overview/crypto-x-ai">
  Today's developers have unprecedented access to AI tools for creating
  responsive, tailored user experiences. At the same time, maintaining AI
  systems that are transparent, unbiased, and free from undue control has become
  more crucial than ever.
</Card>

### Infernet is a *compute powerhouse*

Ritual launched
[Infernet](https://docs.ritual.net/infernet/general/introduction) in November
2023 as the first *decentralized oracle network* for purpose-built AI workloads.

Infernet was designed as a lightweight framework, powered by a network of
[Infernet nodes](https://docs.ritual.net/infernet/node/introduction) executing
arbitrary workload containers. With the `1.0.0` upgrade, we introduced highly
requested features including:
[audited](https://github.com/ritual-net/infernet-sdk/tree/main/audits/v1.1.0)
[on-chain payments](https://docs.ritual.net/infernet/general/payments),
frameworks for
[verification of compute](https://docs.ritual.net/infernet/general/proofs), and
support for
[streaming responses](https://docs.ritual.net/infernet/node/reference/api#post-apijobsstream).

Today, there are **8,000+ independent Infernet nodes**, all with diverse
hardware profiles and capabilities, ready to execute requests. This is **without
any expectation of incentives**.

## Bridging Infernet ↔︎ Chain

### Infernet shortcomings

Noticeably, when architecting Infernet, we explicitly opted for a design that
was
[simple yet flexible](https://docs.ritual.net/infernet/general/introduction#simple-yet-flexible),
forgoing things like coordinating nodes through consensus or integrating a
robust job routing mechanism.

While this enabled us to quickly onboard thousands of compute providers and
iterate on and validate novel, on-chain AI applications with builders, it
inhibited adoption from a broad set of Web2 and Web3 developers.

### Chain-as-an-interface

The combination of the trustless properties of Ritual Chain with the expressive
compute of the Infernet mesh solves these shortcomings to enable truly
transparent AI:

1. We extend [Resonance](/whats-new/resonance) to enable routing compute
   requests to Infernet nodes. This enables an out-of-the-box, robust pricing
   and routing mechanism for Infernet.
2. We extend [execution sidecars](/architecture/execution-sidecars) to tap into
   the broad Infernet mesh for underlying compute.
3. We introduce flexible Web2 adapters that conform to common centralized API
   schemas, but abstract underlying requests silently orchestrated by Ritual
   Chain, with the same strong privacy and verifiability guardrails offered to
   [on-chain AI inference](/whats-new/evm++-sidecars/ai-inference/llm-inference).
4. We enable Web2 requests to, for the first time, be verifiable and
   reproducible through
   [modular computational integrity](/whats-new/ai-primitives/modular-computational-integrity)
   primitives.

For Infernet node operators, this is a seamless upgrade, hyperscaling their
workload demand and proportional earnings.

For Web2 and Web3 users, this is a drop-in replacement to their existing
workloads offering competitively priced, redundantly orchestrated, and private
and verifiable compute.

## Looking forward

As we enable [long-running precompiles](/architecture/evm++#looking-forward) in
Ritual, offloading asynchronous execution to the Infernet mesh will enable a
lazy path to consuming computationally demanding work, while continuing to
inherit the properties of the chain.
