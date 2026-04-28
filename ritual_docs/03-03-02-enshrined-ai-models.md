> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enshrined on-chain AI Models

> Enabling native smart contract interactions with AI models.

export const Spacer = ({gap}) => <div style={{
  marginTop: `${gap}px`
}}></div>;

## Overview

Traditional blockchain networks treat AI models as external resources, accessed
through oracles or off-chain services. This creates a disconnect between smart
contracts and the AI models they interact with, limiting the potential for truly
decentralized AI applications.

Ritual takes a fundamentally different approach by making AI models
**first-class citizens** on the blockchain, enabling atomic interactions between
smart contracts and models.

<Check>
  Just as smart contracts revolutionized digital coordination, enshrined AI
  models enable a new paradigm of programmatic AI interactions with
  cryptographic guarantees.
</Check>

***

## Key functionality

<CardGroup cols={1}>
  <Card title="Native Model Representation" icon="handshake">
    Models exist as on-chain objects with:

    <Spacer gap={10} />

    <Icon icon="check" iconType="solid" /> [Verifiable provenance](/whats-new/ai-primitives/verifiable-provenance)

    <Icon icon="check" iconType="solid" /> Modular model authenticity

    <Icon icon="check" iconType="solid" /> Direct smart contract integration
  </Card>

  <Card title="Atomic Contract-Model Interaction" icon="arrows-cross">
    Enables powerful primitives like:

    <Spacer gap={10} />

    <Icon icon="check" iconType="solid" /> Model inference as part of transaction execution

    <Icon icon="check" iconType="solid" /> Conditional transactions based on model outputs

    <Icon icon="check" iconType="solid" /> Model-driven state transitions
  </Card>

  <Card title="Decentralized Infrastructure" icon="webhook">
    Built on Ritual's core components:

    <Spacer gap={10} />

    <Icon icon="check" iconType="solid" /> [Modular storage layers](/whats-new/modular-storage) for model artifacts

    <Icon icon="check" iconType="solid" /> [Verifiable execution](/whats-new/ai-primitives/modular-computational-integrity) through ZK, TEEs, and more

    <Icon icon="check" iconType="solid" /> [Native model marketplaces](/beyond-crypto-x-ai/model-marketplace) to track and trade models
  </Card>
</CardGroup>

***

## Current State

<Tabs>
  <Tab title="Available Today">
    * Model registration and verification
    * Basic model ownership primitives
    * Verifiable inference execution
    * Integration with [Symphony](/architecture/symphony) for scaling
  </Tab>

  <Tab title="Coming Soon">
    * Advanced model composition
    * Cross-chain model sharing
    * Automated model updates
    * Enhanced DeFAI primitives
  </Tab>
</Tabs>

***

## Use cases

<CardGroup cols={2}>
  <Card title="DeFi + AI" icon="coins">
    Automated market making with ML models

    Model-driven portfolio rebalancing

    Risk assessment for undercollateralized lending
  </Card>

  <Card title="Governance" icon="users-gear">
    DAO proposal analysis

    Automated policy enforcement

    Sentiment-driven treasury management
  </Card>

  <Card title="Gaming" icon="gamepad">
    NPC behavior models

    Dynamic content generation

    Player behavior analysis
  </Card>

  <Card title="Creator Economy" icon="palette">
    Generative art models

    Content moderation

    Personalization engines
  </Card>
</CardGroup>

***

## Getting Started

Get started with consuming models with our
[Classical ML](/whats-new/evm++-sidecars/ai-inference/classical-ml-inference)
and [LLM](/whats-new/evm++-sidecars/ai-inference/llm-inference) Inference
sidecars.

Our [tutorials & case studies](/build-on-ritual/tutorials/lending-protocols)
feature hands-on ways to use native on-chain AI models, tapping into our
enshrined compute and robust primitives.
