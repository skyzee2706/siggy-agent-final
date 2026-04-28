> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Modular Computational Integrity

> Choose the computational integrity gadgets best fit for your application.

<Info>
  Computational integrity is a fundamental property that ensures the output of a
  computation is provably correct and has been executed as intended.
</Info>

<Warning>
  The status quo today forces users to trust centralized AI operators to run
  models correctly without manipulating their inputs or cheating them with worse
  models.
</Warning>

<Check>
  Verifiable computing, powered by the computational integrity gadgets below,
  enables any computation—whether conducted by a trusted or untrusted party—to
  be verified for accuracy and correctness, without redoing the often complex
  computation itself.
</Check>

***

Ritual takes a **credibly-neutral approach** to computational integrity by
enabling users to leverage different gadgets based on their app specific needs
and their willingness to pay.

<Frame caption="Ritual's modular design and flexible underlying architecture empower user choice.">
  <img src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=46284b35435478ef962c84aaefb1f374" alt="Modular primitives" data-og-width="1200" width="1200" data-og-height="675" height="675" data-path="assets/images/modular-primitives.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3d7be9905b842bdd5bc47f778019e82e 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ce226a8a33cb702aa25dcf2d444b51dd 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=afeddd5ab60e5a838f4f80f63863bf00 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=e4aff7b07d3face08e651d71db838319 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=d9ed6a38ae043263ebea1eedfce0af40 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/modular-primitives.svg?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=952f1dca57e6b03cf679c32e1cdb7906 2500w" />
</Frame>

## Supported gadgets

<CardGroup cols={2}>
  <Card title="Zero Knowledge Machine Learning" icon="square-root-variable" href="/whats-new/ai-primitives/modular-computational-integrity#zero-knowledge-machine-learning">
    Strong cryptographic guarantees of correct model execution, at expense of
    added overhead, complexity, and cost.
  </Card>

  <Card title="Optimistic Machine Learning" icon="hand-fingers-crossed" href="/whats-new/ai-primitives/modular-computational-integrity#optimistic-machine-learning">
    Optimistic acceptance of model execution, with model bisection based
    verification only when disputes arise.
  </Card>

  <Card title="Trusted Execution Environments" icon="microchip" href="/whats-new/ai-primitives/modular-computational-integrity#trusted-execution-environments">
    Model execution with hardware-level isolation in enclaves, at expense of
    trust in chip manufacturers and hardware attacks.
  </Card>

  <Card title="Probabilistic Proof Machine Learning" icon="chart-scatter" href="/whats-new/ai-primitives/modular-computational-integrity#probabilistic-proof-machine-learning">
    Low overhead and cost-efficient statistical guarantees of model execution,
    at expense of consistently perfect verification.
  </Card>
</CardGroup>

### Eager vs Lazy consumption

Ritual enables both eager and lazy consumption of proofs from supported gadgets.
Lazy consumption enables use cases where computational integrity is only
required in the sad path:

<Card>
  <Icon icon="plus" iconType="solid" /> **Save costs**: Lazy proofs are
  generated only when disputes or errors occur

  {" "}

  <Icon icon="plus" iconType="solid" /> **Improve performance**: Minimize proof verification
  for applications with infrequent disputes

  <Icon icon="plus" iconType="solid" /> **Better developer experience**: Build
  simpler, easier to audit applications with fewer hot paths
</Card>

***

## Gadget trade-offs

A one-size-fits-all paradigm to computational integrity creates inherent
trade-offs between **security, cost, and performance**. Each gadget has its own
trade-offs and best use cases:

### <Icon icon="square-root-variable" iconType="solid" size={25} />{" "} Zero Knowledge Machine Learning

Zero Knowledge Machine Learning (ZKML) builds on
[zero-knowledge proofs](https://en.wikipedia.org/wiki/Zero-knowledge_proof) to
cryptographically assert correct execution of an AI model.

Ritual's
[ZK generation and verification sidecars](/whats-new/evm++-sidecars/zk-proving-and-verification)
enshrine this gadget natively, enabling users to make strong assertions of model
correctness, with robust blockchain liveness and safety.

<Card>
  <Icon icon="plus" iconType="solid" /> **Robust security**: Offers the
  strongest correctness guarantees via cryptography

  {" "}

  <Icon icon="minus" iconType="solid" color="red" /> **High complexity**: Computationally
  expensive, demands high resources, and is slowest

  <Icon icon="minus" iconType="solid" color="red" /> **Limited support**: Only simple models are supported by modern ZKML proving systems today
</Card>

### <Icon icon="hand-fingers-crossed" iconType="solid" size={20} />{" "} Optimistic Machine Learning

Optimistic Machine Learning (OPML), inspired by
[optimistic rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/),
assumes model execution is correct by default, with verification occurring only
when disputes arise.

At a high level, the system works as follows:

1. Model execution servers stake capital to participate
2. These servers then execute operations, periodically committing intermediary
   outputs
3. If users doubt correctness, they can contest outputs via a fraud proof system
4. The system views models as sequences of functions and uses an **interactive
   bisection** approach, checking layer by layer, to identify output
   inconsistencies
5. If model execution is indeed incorrect, server stake is slashed

<Card>
  <Icon icon="plus" iconType="solid" /> **Cost effective**: Especially efficient for use cases where disputes rarely occur

  {" "}

  <Icon icon="plus" iconType="solid" /> **Extended support**: Bisection approach better
  supports large, complex models (like LLMs)

  {" "}

  <Icon icon="minus" iconType="solid" color="red" /> **Weaker security**: Relies on
  incentivized behavior rather than cryptographic security

  <Icon icon="minus" iconType="solid" color="red" /> **Complex sad path**: Dispute resolution is lengthy, complex, and demands some re-execution
</Card>

### <Icon icon="microchip" iconType="solid" size={20} />{" "} Trusted Execution Environments

Trusted Execution Environments (TEEs) provide hardware-based secure computing
through isolated execution zones where sensitive code and data remain protected.

Ritual's [TEE Execution sidecar](/whats-new/evm++-sidecars/tee-execution)
enshrines this gadget natively by executing AI models in secure enclaves
enabling data confidentiality and preventing model tampering.

<Card>
  <Icon icon="plus" iconType="solid" /> **Performant**: Enables sans-gadget competitive performance for most AI model types

  {" "}

  <Icon icon="plus" iconType="solid" /> **Real-time**: Better suited for real-time
  applications with limited proving complexity or overhead

  {" "}

  <Icon icon="minus" iconType="solid" color="red" /> **Vendor trust**: Requires trust
  in chip manufacturers and secure enclave software

  <Icon icon="minus" iconType="solid" color="red" /> **Hardware attacks**: Susceptible to sophisticated side-channel hardware attacks
</Card>

### <Icon icon="chart-scatter" iconType="solid" size={20} />{" "} Probabilistic Proof Machine Learning

Most model operations are computationally complex, especially when performing
resource-intensive operations like fine-tuning or inference of modern LLMs.

To better support these operations with a low computational overhead tool,
**Ritual has pioneered a new class of verification gadgets**, dubbed
Probabilistic Proof Machine Learning.

The first of this line of tools is [vTune](https://arxiv.org/abs/2411.06611), a
new way to verify LLM fine-tuning through backdoors.

<Card>
  <Icon icon="plus" iconType="solid" /> **Computationally cheap**: Time and cost-efficient for even the most complex model operations

  {" "}

  <Icon icon="plus" iconType="solid" /> **Third-party support**: Suitable for trustlessly
  verifying third-party model API execution

  <Icon icon="minus" iconType="solid" color="red" /> **Statistical correctness**: Not suitable for when perfect verification guarantees are necessary
</Card>

***

## Powered by Ritual

This flexibility of enabling applications to pick and choose from a range of
specialized gadgets is **only possible on Ritual**, built on our belief that
[we should remain proof system agnostic](https://x.com/akileshpotti/status/1758262938257825862).

Powering this belief is our underlying architectural work with
[Resonance](/whats-new/resonance), [Symphony](/whats-new/symphony),
[enshrined execution sidecars](/architecture/execution-sidecars),
[vTune](/whats-new/ai-primitives/verifiable-provenance), Cascade, and more.
