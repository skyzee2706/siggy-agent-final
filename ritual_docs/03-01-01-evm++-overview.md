> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# EVM++

> EVM++ is a backwards-compatible extension of the [Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/) with expressive compute precompiles to build _actually smart_ contracts, with native scheduling, built-in account abstraction, and the most wanted EIPs.

<Frame>
  <img src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=cfaced3ffe7a549b92d0fee5a1fb0926" alt="EVM++ diagram" data-og-width="1200" width="1200" data-og-height="675" height="675" data-path="assets/images/evm-pp.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3d3adac556ab3958ef8928dc42084b27 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=676323be975eea3a113f02279f6cc4dc 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=54d504b79f3b3fbce2e90df9876a4dce 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3b70a7ff1772833937f634f80f6774aa 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=bcfdb2ae3f3b26684ef3f01bc4bb79f6 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/evm-pp.svg?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=04f871088b5f0f8eee0bc7ba6db7dea6 2500w" />
</Frame>

## Core components

### Native scheduling

We introduce a new predeploy contract, dubbed `Scheduler` that enables
developers to register a callback frequency at which their smart contract entry
point is invoked.

Block producers maintain a mapping of pending invocations and may include these
transactions at the top of each block, subject to transaction validity and
sufficient fees.

For heterogeneous or compute-intensive scheduled transactions,
[Resonance](/architecture/resonance) ensures timely allocation and inclusion in
a state-preserving manner.

<Card title="Scheduled Transactions" icon="repeat" href="/architecture/scheduled-transactions" horizontal>
  Recurring, conditional execution of transactions without external keepers.
</Card>

### Account Abstraction

Account Abstraction attempts to blur the line between EOAs and smart contract
accounts, by enabling users to replace their EOA accounts with programmatic
functionality.

We bring native account abstraction support via inclusion of
[EIP-7702: Set EOA Account Code](https://eips.ethereum.org/EIPS/eip-7702).

<Card title="Account Abstraction" icon="user-astronaut" href="/whats-new/evm++/account-abstraction" horizontal>
  Native smart contract accounts via `EIP-7702: SetCodeTx`.
</Card>

### EIP Extensions

Historically, Ethereum and other EVM-based chains have lagged in their support
for integrating novel
[Ethereum Improvement Proposals (EIPs)](https://eips.ethereum.org/), often due
to development overhead or naive gas pricing support for precompiles.

EIP Extensions are our attempt to prioritize continual support and inclusion of
in-demand EIPs that improve user and developer experience.

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

At the heart of EVM++ is our addition of heterogeneous compute precompiles that
allow developers to build net-new applications.

For those familiar with EVM-based smart contract development, using these
compute paradigms maintains the same developer experience as interacting with a
precompile contract.

Behind these standard interfaces are our
[optimized sidecars](/architecture/execution-sidecars) which generate execution
outputs and necessary proofs, consumed by a Ritual execution client.

Because of our standardized interface, generic sidecar architecture, and novel
[Resonance fee mechanism](/architecture/resonance), supporting new heterogeneous
compute precompiles or other execution environments (SVM, MoveVM, etc.) is
naturally supported.

<Card title="Execution Sidecars" icon="sitemap" href="/architecture/execution-sidecars" horizontal>
  Optimized underlying architecture for any type of heterogeneous compute,
  including AI inference, ZK proof verification, TEE code execution, and beyond.
</Card>

## Looking forward

As we continue expanding the set of supported precompiles in EVM++, we'll also
enable long-running precompiles. Via native asynchronous execution, users will
be able to leverage Ritual in a lazy way for more computationally demanding
work, while continuing to inherit the properties of the chain.
