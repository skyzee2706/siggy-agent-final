> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

## Blockchain Fundamentals

**Blockchain**: A decentralized, append-only database that maintains a
cryptographically secured chain of blocks containing transaction records. Each
block is linked to its predecessor through cryptographic hashing, ensuring
immutability and transparency across the network.

**Smart Contract**: Self-executing computer programs on a blockchain that
automatically enforce and execute agreements. Think of them as digital vending
machines that run exactly as programmed.

**L1 (Layer 1)**: A base blockchain network like Ethereum or Ritual Chain that
handles its own transaction validation and security.

**On-chain**: Data or computations that exist directly on the blockchain's
virtual machine.

**Off-chain**: Data or computations that exist outside the blockchain's virtual
machine, and are brought on-chain as needed.

**Cross-chain**: The ability to execute transactions and transfer assets between
different blockchain networks while maintaining security and atomicity. This
enables interoperability and composability across diverse blockchain ecosystems.
See how we enable this in
[Chain Abstraction](/whats-new/evm++-sidecars/chain-abstraction).

**EOA (Externally Owned Account)**: A regular blockchain account controlled by a
private key, like your personal wallet.

**Staking**: The process of locking up tokens as collateral to participate in
network consensus, validation, or other protocol functions. Staked tokens can be
slashed for malicious behavior, creating economic security. Related to our
[Economic Design](/roadmap/going#economic-design).

**ZK (Zero-Knowledge) Proof**: A method to prove something is true without
revealing the underlying information.

***

## Core Protocol Components

**EVM**: The Ethereum Virtual Machine, a Turing-complete state machine that
executes smart contract bytecode in a sandboxed environment. It maintains
deterministic execution across all network nodes while managing gas consumption
and state transitions. Learn more about our extended version at
[EVM++](/whats-new/evm++/overview).

**EVM++**: Ritual's enhanced version of the EVM that adds native support for AI
operations, scheduled transactions, and advanced features while maintaining
backward compatibility. This enables sophisticated smart contracts with built-in
AI capabilities. Learn more in [EVM++ Overview](/whats-new/evm++/overview).

**Symphony Protocol**: A consensus protocol that implements dual proof sharding,
distributed verification, and optimal sampling to reduce redundant execution. It
enables the execute-once-verify-many-times paradigm while maintaining security
guarantees. Learn more in [Symphony](/whats-new/symphony).

**Resonance Mechanism**: A dynamic fee mechanism that matches compute supply
with demand through a market-driven approach. It optimizes resource allocation
by considering workload characteristics and node specialization. See details in
[Resonance](/whats-new/resonance).

**EOVMT (Execute-Once-Verify-Many-Times)**: An optimization protocol where
complex computations are executed by one node and verified efficiently by others
through cryptographic proofs. This reduces network-wide computational redundancy
while maintaining security. Learn more in [Symphony](/architecture/symphony).

***

## Network Architecture

**Node Specialization**: A network architecture that allows nodes to optimize
for specific types of computation (AI, ZK, TEE) while maintaining network
consensus participation. This enables efficient resource allocation and parallel
processing of heterogeneous workloads. Learn more in
[Node Specialization](/whats-new/node-specialization).

**Proof Sharding**: A technique in Symphony that distributes the verification of
computation proofs across different node subsets to improve scalability and
efficiency. See our implementation in
[Symphony](/architecture/symphony#distributed-verification-via-partitioned-proofs).

**Distributed Verification System**: A component of Symphony that enables
efficient verification of complex computations through proof partitioning and
committee-based consensus. See our approach in
[Symphony](/architecture/symphony#distributed-verification-via-partitioned-proofs).

**Execution Sidecar**: A modular component that handles specialized computation
tasks asynchronously from the main chain. Sidecars enable complex operations
while maintaining EVM compatibility and security guarantees. Learn more in
[Execution Sidecars](/architecture/execution-sidecars).

**Chain Abstraction Layer**: A protocol layer that enables seamless interaction
between different blockchain networks while maintaining security and consistency
guarantees. See details in
[Chain Abstraction](/whats-new/evm++-sidecars/chain-abstraction).

***

## AI and Model Infrastructure

**Model Inference**: The process of using a trained AI model to generate outputs
from new inputs. This includes preprocessing inputs, running them through the
model's computational graph, and post-processing outputs. Learn about our
implementation in [AI Primitives](/whats-new/ai-primitives/enshrined-ai-models).

**Fine-tuning**: A machine learning technique that adapts a pre-trained model to
a specific task by updating its parameters with new data. This preserves the
model's base knowledge while optimizing for targeted use cases. See our approach
in [AI Primitives](/whats-new/ai-primitives/enshrined-ai-models).

**Verifiable Model Training**: The process of training AI models with
cryptographic guarantees of correctness and provenance, using techniques like
watermarking and backdoors. Learn more in
[Verifiable Provenance](/whats-new/ai-primitives/verifiable-provenance).

**Enshrined Model**: An AI model that is natively represented on-chain as a
first-class citizen, enabling direct smart contract integration and verifiable
execution. Learn more in
[Enshrined AI Models](/whats-new/ai-primitives/enshrined-ai-models).

***

## Verification and Privacy

**TEE (Trusted Execution Environment)**: A secure hardware enclave that isolates
sensitive computations from the main system. TEEs provide confidentiality and
integrity guarantees through hardware-based encryption and attestation. See our
implementation in [TEE Execution](/whats-new/evm++-sidecars/tee-execution).

**ZKML (Zero-Knowledge ML)**: A system that combines zero-knowledge proofs with
machine learning to verify model computations without revealing inputs, weights,
or intermediate values. This enables private and verifiable AI execution. See
our implementation in
[ZK Proving and Verification](/whats-new/evm++-sidecars/zk-proving-and-verification).

**OPML (Optimistic-ML)**: A verification system that assumes AI computations are
correct by default but allows for challenge periods. Challengers can dispute
results by providing counter-examples, leading to efficient verification of
large models. See [AI Primitives](/whats-new/ai-primitives/enshrined-ai-models).

**PPML (Probabilistic Proof ML)**: A verification approach that uses statistical
properties and backdoors in ML models to prove training authenticity and detect
unauthorized modifications. This provides efficient verification for model
provenance. Learn more in
[Verifiable Provenance](/whats-new/ai-primitives/verifiable-provenance).

**Modular Computational Integrity**: A flexible system that allows developers to
choose and combine different verification approaches (ZKML, OPML, PPML) based on
their specific needs. See our implementation in
[Modular Computational Integrity](/whats-new/ai-primitives/modular-computational-integrity).

***

## Platform Features

**Oracle**: A bridge between blockchains and external data sources that enables
smart contracts to access off-chain information in a secure and verifiable way.
Oracles validate and authenticate external data before making it available
on-chain. See how Ritual implements oracles in
[Enshrined Oracles](/whats-new/enshrined-oracles/infernet-to-world).

**Infernet**: A decentralized oracle network specifically designed for bringing
verified AI computation on-chain. It provides secure model execution, result
verification, and cross-chain integration capabilities. See
[Infernet to Chain](/architecture/infernet-to-chain).

**Agent Launchpad**: A platform for deploying and managing autonomous agents
with built-in economic incentives and security guarantees. It provides
standardized interfaces and safety mechanisms for agent-protocol interactions.
See [Agents](/whats-new/agents).

**Model Registry**: A decentralized system for registering, tracking, and
managing AI models on-chain. It handles model versioning, ownership, and
provenance verification. Learn more in
[Enshrined AI Models](/whats-new/ai-primitives/enshrined-ai-models).

**Model Marketplace**: A decentralized platform for trading AI models with
built-in provenance tracking, licensing, and automated revenue distribution.
Learn more in [Model Marketplace](/beyond-crypto-x-ai/model-marketplace).

**Ritual Guardians**: A specialized node system that monitors network health and
verifies complex computations. Guardians form a security layer complementing
traditional validators, particularly for heterogeneous workloads. See
[Guardians](/whats-new/guardians).

**Ritual Portals**: Cross-chain bridges built on GMP protocols that enable
secure access to Ritual's specialized compute capabilities from any blockchain.
Portals handle message verification, state synchronization, and result delivery.
Learn more in [Ritual to World](/architecture/ritual-to-world).

**Modular Storage**: A flexible storage architecture that supports multiple
backend solutions while providing a unified interface for developers. This
enables optimization for different data types while maintaining consistency and
availability. See [Modular Storage](/whats-new/modular-storage).

**Provenance**: A comprehensive system for tracking and verifying the complete
lifecycle of digital assets, including creation, ownership transfers, and
modifications. This enables trust and accountability in decentralized systems.
See our approach in
[Verifiable Provenance](/whats-new/ai-primitives/verifiable-provenance).
