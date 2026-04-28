> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Expressive Blockchains

> Ritual's unique architecture enables it to power more than just Crypto x AI use-cases, becoming the schelling point for all of Web3.

## Beyond Crypto x AI

While Ritual excels at
[enabling state-of-the-art AI applications](/build-on-ritual/case-studies/ai-stablecoin),
our underlying architecture is optimized for all types of heterogeneous compute
(including
[ZK, TEE, Chain Abstraction, and more](/whats-new/evm++-sidecars/overview)
out-of-the-box).

Fundamental innovations like [Resonance](/architecture/resonance),
[Symphony](/architecture/symphony), and
[Ritual ↔︎ World](/architecture/ritual-to-world) enable:

1. Efficiently **pricing any type of compute**, without chain fee mechanism
   modifications
2. **Node specialization** enabling broad classes of participants and workloads
3. Consuming Ritual compute from **any chain**, with **verifiable outputs**

## Why Expressive Blockchains?

Traditional blockchain architectures were designed for homogeneous
transactions—simple transfers and basic smart contract interactions where every
node executes the same computation. However, the Web3 landscape is rapidly
evolving:

* **Complex Computations**: Modern blockchain applications demand increasingly
  sophisticated operations, from ZK proofs to ML inference
* **Specialized Hardware**: Different types of computation benefit from
  specialized hardware (GPUs, TPUs, FPGAs, ASICs)
* **Resource Intensity**: Heavy computational tasks like proof generation or
  model inference are inefficient when replicated across all nodes
* **Cost Efficiency**: Forcing all nodes to execute all computations leads to
  higher network execution costs and reduced throughput

This evolution demands a new paradigm: one where blockchain networks can
efficiently handle heterogeneous computation while maintaining security and
decentralization.

***

## Ritual Architecture

Three key architectural innovations make Ritual the ideal venue for expressive
blockchain computation:

### Resonance

[Resonance](/architecture/resonance) introduces a surplus-maximizing transaction
fee mechanism that efficiently matches user transactions with specialized
compute nodes. Unlike traditional blockchain architectures where all nodes
execute all transactions, Resonance enables:

* Selective execution based on node specialization
* Private, unique execution cost functions for compute providers
* Efficient price discovery through sophisticated brokers

### Symphony

[Symphony](/architecture/symphony) is a new state-of-the-art consensus protocol
that builds upon proven consensus mechanisms while introducing:

* Dual proof sharding for reduced replicated execution
* Distributed verification for high-performance workloads
* Optimized committee election for specialized compute tasks

### Ritual ↔︎ World

Our [Ritual ↔︎ World](/architecture/ritual-to-world) integrations enable other
blockchains to tap into Ritual's infrastructure as a backend for their own
execution, outsourcing their heterogeneous computation to Ritual's optimized
execution environment.

* Simple integration for any blockchain network via
  [Infernet](/architecture/infernet-to-chain) or GMP
* Out-of-the-box support for all types of compute (ZK, TEE, Chain Abstraction,
  etc.)
* Optimized pricing, routing, and execution via Ritual architecture

***

## Ritual-as-a-backend

Other blockchain networks can tap into Ritual's infrastructure in several ways:

### Direct Integration

Other chains can directly connect to Ritual's compute mesh through:

* **Message Passing**: Standard cross-chain communication protocols to request
  compute
* **Infernet Integration**: Direct access via Ritual's 8,000+ specialized
  compute nodes

### Compute Outsourcing

Chains can offload specific computational tasks to Ritual:

* **Proof Generation**: For ZK-rollups and other proving systems
* **Model Inference**: For AI/ML workloads
* **TEE**: For trusted execution environments
* **Optimized execution pricing**: For L2 RaaS providers, via Resonance
* **Custom Compute**: For any specialized computational needs

### Benefits

By leveraging Ritual's infrastructure, chains gain:

* **Cost Efficiency**: Pay only for the compute they need
* **Specialized Hardware**: Access to a diverse network of compute providers
* **Scalability**: Offload heavy computation without sacrificing
  decentralization
* **Future-Proofing**: Support for new types of computation as they emerge

***

## Initial applications

This unique architecture positions Ritual as the backbone for next-generation
blockchain applications. In the following sections, we explore three key
use-cases that showcase how Ritual's infrastructure powers applications beyond
Crypto x AI:

<CardGroup cols={1}>
  <Card title="Prover Networks" icon="lambda" href="/beyond-crypto-x-ai/prover-networks" wide>
    High-performance chains can leverage Ritual for efficient proof generation
    and verification.
  </Card>

  <Card title="L2 RaaS" icon="layer-group" href="/beyond-crypto-x-ai/l2-raas" wide>
    Enabling modern Rollup-as-a-Service offerings through heterogeneous compute
    orchestration.
  </Card>

  <Card title="Model Marketplace" icon="store" href="/beyond-crypto-x-ai/model-marketplace" wide>
    Creating a verifiable marketplace for intellectual property and compute
    assets.
  </Card>
</CardGroup>

Through these innovations, Ritual becomes more than just a platform—it evolves
into the schelling point for Web3's most demanding computational needs, current
and future.
