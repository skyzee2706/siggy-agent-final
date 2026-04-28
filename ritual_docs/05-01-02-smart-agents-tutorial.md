> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Agents

> Build verifiable, autonomous agents with proveable execution, cross-chain capabilities, and on-chain action provenance.

***

## The Agent Challenge

AI Agents represent the frontier of Crypto × AI, operating with independence
making decisions, and taking on-chain actions without human intervention.

In 2023, **we pioneered the idea of on-chain AI agents** with
[Frenrug](https://www.frenrug.com/), an agent controlled by a combination of LLM
and Classical ML models,
[managing over \$30,000 on Base](https://basescan.org/address/0x5bfe1Ed1741c690eC3e42795cf06a4c38Ed3BC0c).

Yet, while recent traction has pushed the
[agents market cap past \$13B](https://www.cookie.fun/), current, leading
**agents and agent frameworks have regressed** to poor, unsophisticated
implementations, limited in their capabilities:

1. **Trust & Verification**: No reliable way to verify autonomous operation or
   decision-making
2. **Limited Capabilities**: Restricted action space and poor integration with
   external services
3. **Security Risks**: Vulnerable to model and private key tampering and
   unauthorized access
4. **Centralized Control**: Reliance on centralized providers for model and
   trade execution
5. **Privacy Concerns**: User data and agent behavior exposed to central
   operators
6. **Poor Composability**: Limited ability to coordinate between multiple agents
7. **Difficult Developer Experience**: Poor framework architectures force
   simple, fragile agents
8. **Inadequate Architecture**: Poor reproducibility, broken state consistency,
   unsafe parallelism

***

## Existing landscape

As a part of our exploration, we explored the existing Web2 and Web3 agents and
agent framework and tooling ecosystems, closely studying projects including:
[elizaOS](https://elizaos.ai/), [AI Rig Complex](https://www.arc.fun/),
[autogen](https://github.com/microsoft/autogen),
[Coinbase Agent Kit](https://www.coinbase.com/developer-platform/discover/launches/introducing-agentkit),
[ZerePy](https://github.com/blorm-network/ZerePy),
[DSPy](https://github.com/stanfordnlp/dspy),
[multi-agent-orchestrator](https://github.com/awslabs/multi-agent-orchestrator),
[GOAT SDK](https://github.com/goat-sdk/goat),
[Llama Agents](https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems),
[Heurist](https://agent.heurist.ai/),
[Virtuals](https://www.virtuals.io/protocol),
[Solana Agent Kit](https://github.com/sendaifun/solana-agent-kit),
[CrewAI](https://www.crewai.com/),
[TapeAgents](https://github.com/ServiceNow/TapeAgents),
[Nexus](https://gpt.nexus/), [Swarms](https://docs.swarms.world/en/latest/),
[BabyAgi2](https://github.com/yoheinakajima/babyagi-2o),
[LangChain](https://www.langchain.com/),
[Aether](https://github.com/AetherFrameworkAI/aether-framework),
[Sora](https://github.com/soralabs),
[Allice](https://github.com/myshell-ai/AIlice),
[Nous Agents](https://github.com/NousResearch/nousflash-agents),
[Cline](https://github.com/cline/cline),
[OpenAI Swarm](https://github.com/openai/swarm),
[DuckAI](https://github.com/fatduckai/ai).

Our research identified several key patterns and challenges:

<Tabs>
  <Tab title="Architecture">
    In the ideal world, agents follow a linear, reproducible architecture:

    1. Agent **observes** world state
    2. Agent **updates** internal state
    3. Agent **takes actions**

    Yet, in our exploration, we found that many frameworks break this model by:

    1. Allowing observation components to take direct actions
    2. Hindering reproducibility of agent actions
    3. Operating unsafely in a parallel environment, causing undue race conditions
    4. Breaking state consistency across agent actions
    5. Interspersing sync and async agent processing
  </Tab>

  <Tab title="Security">
    Holistically, we found that no current frameworks adequately address privacy and authentication concerns. Frequently, we found agent wallets to be controlled by humans in the loop, or poor handling of secure key data.

    <CardGroup cols={2}>
      <Card title="Limited Credential Management" icon="key">
        Secure handling of key material and API data remains a critical challenge. Most agents do not run in TEEs and private key material is exposed to developers.
      </Card>

      <Card title="Poor Data Privacy" icon="shield-slash">
        Balancing data privacy and using centralized AI providers to maximize agent usability and performance presents a dilemma.
      </Card>
    </CardGroup>
  </Tab>
</Tabs>

***

## Ritual's Agent Framework

Ritual provides a comprehensive framework for **building better agents**, that
are verifiable, truly autonomous, and cross-chain.

On top, our **upcoming agent launchpad** simplifies the lifecycle of building
and orchestrating complex agents, while tapping into the secure underlying
execution properties of Ritual Chain.

### Enhanced Capabilities

Agents on Ritual **live on-chain**, with all execution logic (AI Inference, TEE
code execution, wallet management, cross-chain trading, etc.) happening directly
within a smart contract.

<CardGroup cols={2}>
  <Card title="Verifiable Execution" icon="shield-check">
    Guaranteed autonomous operation with [TEE execution](/whats-new/evm++-sidecars/tee-execution) and blockchain provenance.
  </Card>

  {" "}

  <Card title="Enshrined AI Inference" icon="microchip-ai">
    Secure, privacy-preserving [AI
    inference](/whats-new/evm++-sidecars/ai-inference/classical-ml-inference)
    powering real-time agent decision-making.
  </Card>

  {" "}

  <Card title="Autonomous Operation" icon="clock">
    [Scheduled transactions](/architecture/scheduled-transactions) orchestrate
    agent lifecycles without keepers or Web2 servers.
  </Card>

  {" "}

  <Card title="Cross-chain Composability" icon="chart-network">
    [Chain Abstraction](/whats-new/evm++-sidecars/chain-abstraction) enables
    agents to take actions across any blockchain network.
  </Card>

  {" "}

  <Card title="Trade & Swap Agent Models" icon="store">
    [Model marketplaces](/beyond-crypto-x-ai/model-marketplace) allow users to
    trade best-performing agent models.
  </Card>

  <Card title="Enhanced Wallet Management" icon="wallet">
    Native [account abstraction](/whats-new/evm++/account-abstraction) enables secure wallet management and delegation.
  </Card>
</CardGroup>

### Autonomous Evolution

Ritual agents have self-improving capabilities:

<Card>
  <Icon icon="check" iconType="solid" /> On-chain adaptation with **verifiable performance gains**

  <Icon icon="check" iconType="solid" /> Adaptive **strategy evolution** via DAOs

  <Icon icon="check" iconType="solid" /> Self-healing through **automated failure detection and recovery**
</Card>

### Multi-Agent Coordination

Ritual Chain acts as a trust-minimized coordination layer for agent-to-agent
communication, enabling complex multi-agent systems with cryptographic
guarantees.

<CardGroup cols={2}>
  <Card title="Communication Layer" icon="network-wired">
    <Icon icon="check" iconType="solid" /> Secure message passing

    <Icon icon="check" iconType="solid" /> State synchronization

    <Icon icon="check" iconType="solid" /> Resource sharing

    <Icon icon="check" iconType="solid" /> Conflict resolution
  </Card>

  <Card title="Coordination Patterns" icon="arrows-split-up-and-left">
    <Icon icon="check" iconType="solid" /> Hierarchical organization

    <Icon icon="check" iconType="solid" /> Peer-to-peer collaboration

    <Icon icon="check" iconType="solid" /> Task delegation

    <Icon icon="check" iconType="solid" /> Collective decision making
  </Card>
</CardGroup>

***

## Future Directions

We plan to continue to extend the capabilities of Ritual agents:

<Steps>
  <Step title="Automated Evolution">
    * Automated skill acquisition
    * Experience synthesis
    * Adaptive specialization
  </Step>

  <Step title="Context Portability">
    * Cross-\{(chain, task)} knowledge transfer
    * Multi-domain expertise
    * Context adaptation
    * Skill composition
  </Step>
</Steps>

***

## Getting Started

You can get started building autonomous, smart agents on Ritual **today**.

Our [tutorials & case studies](/build-on-ritual/case-studies/smart-agents)
feature ways to build infinitely customizable on-chain agents, tapping into our
native enshrined compute and robust primitives.
