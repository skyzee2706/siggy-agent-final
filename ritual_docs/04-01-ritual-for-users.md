> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ritual for Users

> Net-new functionality enabled for users and developers.

## AI Agents

Ritual provides a comprehensive framework for building better agents:

<Card title="Smart Agents" icon="user-bounty-hunter" href="/whats-new/agents" horizontal>
  Build verifiable, autonomous agents with proveable execution and on-chain
  action provenance.
</Card>

## EVM++

Backwards-compatible extension of the EVM to build *actually smart* contracts,
with:

<CardGroup cols={2}>
  <Card title="Native Scheduling" icon="repeat" href="/architecture/scheduled-transactions">
    Recurring, conditional execution of transactions without external keepers.
  </Card>

  <Card title="Account Abstraction" icon="user-astronaut" href="/whats-new/evm++/account-abstraction">
    Native smart contract accounts via `EIP-7702: SetCodeTx`.
  </Card>
</CardGroup>

### EIP Extensions

Early support and inclusion for in-demand EIPs:

<CardGroup cols={2}>
  <Card title="EIP-665" icon="plus" href="/whats-new/evm++/eip-extensions/eip-665">
    Adds support for `Ed25519` signature verification.
  </Card>

  <Card title="EIP-5027" icon="plus" href="/whats-new/evm++/eip-extensions/eip-5027">
    Removes the limit on smart contract code size with new, dynamic gas
    metering.
  </Card>

  <Card title="EIP-5920" icon="plus" href="/whats-new/evm++/eip-extensions/eip-5920">
    Adds a new `PAY` opcode to send ether without transferring execution
    context.
  </Card>

  <Card title="EIP-7212" icon="plus" href="/whats-new/evm++/eip-extensions/eip-7212">
    Adds support for `secp256r1` signature verification.
  </Card>
</CardGroup>

### Expressive compute

Heterogeneous compute precompiles to power net-new applications:

<CardGroup cols={2}>
  <Card icon="link" title="Classical ML Inference" href="/whats-new/evm++-sidecars/ai-inference/classical-ml-inference">
    Leverage canonical tree-based and regression-based models for efficient and
    scalable ML computation.
  </Card>

  <Card icon="link" title="LLM Inference" href="/whats-new/evm++-sidecars/ai-inference/llm-inference">
    Leverage state-of-the-art LLM models for complex language tasks.
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card icon="link" title="ZK Proving & Verification" href="/whats-new/evm++-sidecars/zk-proving-and-verification" horizontal>
    Generate ZK proofs for heterogeneous computation, ensuring verifiable and
    tamper-proof computation.
  </Card>

  <Card icon="link" title="TEE Execution" href="/whats-new/evm++-sidecars/tee-execution" horizontal>
    Perform secure computation in a Trusted Execution Environment (TEE),
    enabling privacy-preserving AI model inference, autonomous & self-evolving
    agents, external API calls, and more.
  </Card>

  <Card icon="link" title="Chain Abstraction" href="/whats-new/evm++-sidecars/chain-abstraction" horizontal>
    Natively read (and in the future, write) state to and from other blockchain
    networks all from Ritual Chain.
  </Card>
</CardGroup>

## AI Primitives

Models as enshrined, first-class blockchain objects backed by a suite of
special-purpose primitives across provenance, privacy, and computational
integrity:

<CardGroup cols={2}>
  <Card title="Modular Computational Integrity" icon="signature-lock" href="/whats-new/ai-primitives/modular-computational-integrity">
    Special-purpose, opt-in primitives across provenance, privacy, and
    computational integrity.
  </Card>

  <Card title="Enshrined On-Chain AI Models" icon="microchip-ai" href="/whats-new/ai-primitives/enshrined-ai-models">
    Train, track, and trade AI models with on-chain provenance, authenticity,
    and IP primitives.
  </Card>

  <Card title="Verifiable Provenance" icon="waveform-lines" href="/whats-new/ai-primitives/verifiable-provenance">
    Immutable records of model origin, updates, and transformations with novel
    provenance innovations.
  </Card>

  <Card title="Model Marketplace" icon="store" href="/beyond-crypto-x-ai/model-marketplace">
    Monetize models transparently with verifiable provenance ensuring security
    and integrity.
  </Card>
</CardGroup>

## Enshrined Oracles

Priority execution for critical, automated operations like oracle updates and
rebalancing mechanisms, with separately priced fee markets:

<CardGroup cols={2}>
  <Card title="Infernet ↔︎ World" icon="chart-network" href="/whats-new/enshrined-oracles/infernet-to-world">
    Enshrined oracles built into the chain, powered by Infernet.
  </Card>

  <Card title="Scheduled Transactions" icon="repeat" href="/whats-new/enshrined-oracles/scheduled-transactions">
    Top-of-block privileged inclusion of scheduled transactions.
  </Card>
</CardGroup>

## and much more...

<CardGroup cols={1}>
  <Card title="Modular Storage" icon="database" href="/whats-new/modular-storage" horizontal>
    Storage-agnostic approach to data, with support for web2 (HuggingFace) and
    web3 (Arweave).
  </Card>

  <Card title="Resonance" icon="intersection" href="/whats-new/resonance" horizontal>
    State-of-the-art surplus-maximizing transaction fee mechanism to efficiently
    match supply and demand, offering users optimally priced transaction
    execution.
  </Card>

  <Card title="Ritual ↔︎ World" icon="globe" href="/architecture/ritual-to-world" horizontal>
    Tap into Ritual's optimized compute offerings and mesh of special-purpose
    nodes from any blockchain network.
  </Card>
</CardGroup>
