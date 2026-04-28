> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Modular Storage

> Storage-agnostic approach to data, with support for Web2 and Web3 venues.

## Current State

Modern blockchains operate with limited, expensive on-chain storage
capabilities:

1. No native integration with external storage systems, centralized or
   decentralized
2. Smart contracts cannot directly access or compute over stored data
3. Complex off-chain infrastructure required for data storage operations
4. Fragmented storage solutions across Web2 and Web3

Ritual operates with large data objects like AI models and features that demand
robust, cost-effective storage and high-performance caches for best performance.

***

### Ritual's Innovation

Ritual introduces a provider-agnostic approach to storage by abstracting storage
access into the familiar concept of **repositories**.

Through initial native integration with both Web2 (via
[Hugging Face Hub](https://huggingface.co/)) and Web3 (via
[Arweave](https://arweave.org/)) storage layers, smart contracts can directly
access and compute over data while maintaining consistent security guarantees.

This unified system enables developers to choose storage solutions based on
their specific needs—whether that's rapid prototyping with familiar web2 tools
or ensuring permanent, censorship-resistant data availability through
decentralized storage.

<Tip>
  Get started with Ritual's modular storage offerings by tapping into our
  [infernet-ml](https://infernet-ml.docs.ritual.net/models/) helper utilities.
</Tip>
