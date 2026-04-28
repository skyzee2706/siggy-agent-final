> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Where everyone else is not going

> What are other chains fundamentally missing that Ritual isn't?

***

### Native, heterogeneous compute

Ritual's thesis is rooted in the defining hypothesis that the complexity of what
you can do on blockchain networks will dramatically grow over time.

To that extent, Ritual is focused on being the **most expressive blockchain
in existence**, hyperscaling the expressive compute that can be performed on a
blockchain.

Ritual firmly believes that developers want to consume this compute via the
tools they are already familiar with, beginning by supporting atomic
heterogeneous operations via the EVM.

<CardGroup cols={2}>
  <Card title="What is Ritual?" icon="question" href="/overview/what-is-ritual">
    Learn more about the most expressive blockchain in existence.
  </Card>

  <Card title="Architecture" icon="connectdevelop" href="/architecture/evm++">
    Dig into the underlying architecture and innovations that power Ritual
    Chain.
  </Card>
</CardGroup>

***

### Flexible verification

Rather than committing to a single verification approach, Ritual is proof system
agnostic. We recognize that different applications have different requirements
for security, cost, and performance. Our modular computational integrity system
lets developers choose and combine:

* [ZKML](/whats-new/evm++-sidecars/zk-proving-and-verification) for maximum
  security and privacy
* [OPML](/whats-new/ai-primitives/modular-computational-integrity) for efficient
  verification of larger models where interaction is acceptable
* [PPML](/whats-new/ai-primitives/modular-computational-integrity) for cheap,
  non-interactive statistical verification through backdoors
* [TEE](/whats-new/evm++-sidecars/tee-execution) for hardware-based security

The goal is to match the right verification strategy to your specific needs, not
force one approach for all use cases.

***

### Node specialization

Traditional blockchains like Ethereum operate by coming to consensus over
ordering and replicated execution of transactions.

Ritual introduces node specialization through architecture purpose-built for
reducing redundant re-execution and enabling user preference, **letting Ritual
scale special-purpose compute**.

<Card icon="circle-nodes" title="Node specialization" href="/whats-new/node-specialization">
  Nodes can specialize in select types of compute including AI Inference, ZK
  Proving, or TEE Code Execution, rather than servicing all operations, earning
  outsized rewards for performance.
</Card>

***

### Long-running, stateful execution

With the extension of execution sidecars to be stateful, Ritual will adopt a
minimally invasive approach to enabling asynchronous execution for long-running
compute precompiles, all orchestrated via the blockchain.

This will enable radically new applications to be built that out-source
long-running, computationally-intensive tasks to a robust network of underlying
compute providers.

<Card title="Execution Sidecars" icon="sitemap" href="/architecture/execution-sidecars" horizontal>
  Optimized underlying architecture for any type of heterogeneous compute,
  including AI inference, ZK proof verification, TEE code execution, and beyond.
</Card>

***

### Web2 adapters

Ritual acts as a drop-in AI Inference API replacement for common Web2 use-cases,
offering competitively priced, redundantly orchestrated, and private and
verifiable compute.

<Card title="Infernet ↔︎ Chain" icon="chart-network" href="/architecture/infernet-to-chain" horizontal>
  Ritual, with its underlying mesh of 8,000+ connected Infernet nodes, lets
  anyone, anywhere tap into transparent AI, with strong privacy and
  verifiability guardrails.
</Card>

***

### Ritual-as-a-service

<Card title="Ritual ↔︎ World" icon="globe" href="/architecture/ritual-to-world" img="/assets/images/ritual-and-world.svg">
  Not only will end-users consume applications natively through Ritual, but
  other blockchains themselves symbiotically benefit by tapping into Ritual
  compute.
</Card>

***

### Robust agentic primitives

Ritual built [Frenrug](https://frenrug.com), the first on-chain AI agent.

Now, we are laying the fundamental groundwork for AI agents that live, interact,
and transact entirely on-chain:

<CardGroup cols={2}>
  <Card icon="link" title="What's new?: EVM++" href="/whats-new/evm++/overview">
    EVM++ is a backwards-compatible extension of the Ethereum Virtual Machine.
  </Card>

  <Card title="Native Scheduling" icon="repeat" href="/architecture/scheduled-transactions">
    Recurring, conditional execution of transactions without external keepers.
  </Card>

  <Card title="Account Abstraction" icon="user-astronaut" href="/whats-new/evm++/account-abstraction">
    Native smart contract accounts via `EIP-7702: SetCodeTx`.
  </Card>

  <Card title="EIP Extensions" icon="plug" href="/whats-new/evm++/eip-extensions/overview">
    Early support for in-demand EIPs.
  </Card>
</CardGroup>
