> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Ritual enables expressive, heterogeneous compute via the EVM precompile contract
interface.

In contrast to Ethereum and other EVM-compatible blockchains today, that
implement precompiles
[directly in their execution client codebases](https://github.com/ethereum/go-ethereum/blob/master/core/vm/contracts.go),
Ritual's compute precompiles are instead implemented as disjoint sidecars that
run and scale **parallel** to an execution client.

With this modular design, anyone that can architect a containerized sidecar can
automatically have their computation be enshrined on-chain.

You can learn more about this architectural decision
[here](/architecture/execution-sidecars).

***

## Supported sidecars

Ritual currently supports a range of EVM++ sidecars designed for specific use
cases, including AI Inference, ZK Proving & Verification, TEE Code Execution,
Agents, and Chain Abstraction.

<CardGroup cols={2}>
  <Card icon="link" title="Classical ML Inference" href="/whats-new/evm++-sidecars/ai-inference/classical-ml-inference">
    Leverage canonical tree-based and regression-based models for efficient and
    scalable ML computation.
  </Card>

  <Card icon="link" title="LLM Inference" href="/whats-new/evm++-sidecars/ai-inference/llm-inference">
    Leverage state-of-the-art LLM models for complex language tasks.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card icon="link" title="ZK Proving & Verification" href="/whats-new/evm++-sidecars/zk-proving-and-verification">
    Generate ZK proofs for heterogeneous computation, ensuring verifiable and
    tamper-proof computation.
  </Card>

  <Card icon="link" title="TEE Execution" href="/whats-new/evm++-sidecars/tee-execution">
    Perform secure computation in a Trusted Execution Environment (TEE),
    enabling privacy-preserving AI model inference, autonomous & self-evolving
    agents, external API calls, and more.
  </Card>

  <Card icon="link" title="Chain Abstraction" href="/whats-new/evm++-sidecars/chain-abstraction">
    Natively read (and in the future, write) state to and from other blockchain
    networks all from Ritual Chain.
  </Card>
</CardGroup>
