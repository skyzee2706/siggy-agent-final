> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Guardians

> Advanced compute firewalls for specialized node operation.

## Background

Traditional blockchain nodes face a fundamental challenge: they must process all
transactions uniformly, regardless of their computational requirements or
content. This creates an inefficient "one-size-fits-all" approach that limits
node operator diversity and network scalability.

### Key limitations

<Steps>
  <Step title="Uniform Computation">
    Traditional nodes must:

    * Process all transactions regardless of complexity
    * Maintain expensive hardware capabilities uniform to network
    * Handle all types of computation equally
  </Step>

  <Step title="Limited Specialization">
    Current networks lack:

    * Node specialization mechanisms
    * Granular compute selection
    * Content-aware transaction processing
  </Step>

  <Step title="Resource Inefficiency">
    This all leads to:

    * Overprovisioned hardware
    * Underutilized resources
    * Reduced operator diversity
  </Step>
</Steps>

***

## Ritual's Solution

Just as traditional firewalls filter network traffic, Ritual Guardians enable
**computational and semantic filtering of blockchain operations**.

These filters empower node operators to **granularly provision** the set of
requests they want to service, **while still maintaining consensus
participation** in the network.

### Computational Firewalls

<Tabs>
  <Tab title="Hardware-based">
    Nodes can filter based on:

    * [AI model size](/whats-new/evm++-sidecars/ai-inference/llm-inference)
    * [ZK circuit complexity](/whats-new/evm++-sidecars/zk-proving-and-verification)
    * [TEE code execution requirements](/whats-new/evm++-sidecars/tee-execution)
  </Tab>

  <Tab title="Resource-based">
    Nodes can dynamically filter by resource requirements:

    * GPU memory thresholds
    * CPU core requirements
    * Network bandwidth needs
  </Tab>
</Tabs>

### Statistical Firewalls

Statistical firewalls **enable nodes to hyperspecialize**, only processing
prompts and workloads that align with their intended use cases. For example, a
node could choose to only process scientific computing tasks that fall within an
embedding distance from core scientific topics.

<Tabs>
  <Tab title="Semantic-based">
    Nodes can semantically filter based on:

    * Prompt categories and topics
    * Model specialization domains
    * Content safety boundaries
  </Tab>

  <Tab title="Metric-based">
    Filter using quantitative measures:

    * Embedding space distances
    * Semantic similarity scores
    * Topic cluster membership
  </Tab>
</Tabs>

### Consensus Preservation

While nodes can opt out of direct computation, they maintain network security
by:

* Verifying succinct proofs from executor nodes
* Participating in [Symphony's](/architecture/symphony) consensus
* Contributing to network diversity
