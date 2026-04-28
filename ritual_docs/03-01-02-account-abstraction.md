> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Abstraction

## Background

Today, [Ethereum](https://ethereum.org/en/developers/docs/accounts/)-based
blockchains support two types of accounts:

1. **Externally-owned accounts (EOAs)**: accounts controlled by ownership of a
   `private key`
2. **Smart contract accounts**: accounts controlled by code deployed to the
   network

Historically, EOA accounts have been limited in their functionality: users can
send and receive blockchain transactions signed by their `private key`(s), and
nothing more.

In contrast, smart contract accounts
[enable limitless functionality](https://www.ithaca.xyz/writings/exp-0001#background),
including:

1. **Batch calls**: Sending multiple transactions at once
2. **Gas fee sponsorship**: Frictionless zero-fee user transactions
3. **Arbitrary signing keys**: Use diverse signature schemes (`P256`, `BLS`,
   etc.)
4. **Advanced ACLs**: Assign granular usage permissions and control access
   lifespans

[Account Abstraction](https://eips.ethereum.org/EIPS/eip-4337) attempts to blur
the line between EOAs and smart contract accounts, by enabling users to replace
their EOA accounts with programmatic functionality.

## EIP-7702

Ritual Chain is one of the earliest blockchains to support
[EIP-7702: Set EOA account code](https://eips.ethereum.org/EIPS/eip-7702), the
leading account abstraction implementation, initially proposed by Vitalik
Buterin.

EIP-7702 adds a new transaction type, `SetCodeTx`, which enables EOA accounts to
delegate a smart contract as their implementation.

Now, in addition to regular EOA functionality, users can also use programmatic
smart contract functionality as if a contract was deployed to their EOA
`address` itself. This is done by signing and sending a transaction to
`address(self)`.

## Reading links

1. [ERC-4337: Account Abstraction](https://www.erc4337.io/)
2. [EIP-7702: Set EOA account code](https://eips.ethereum.org/EIPS/eip-7702)
3. [EXP-0001: Account Delegation with EIP-7702](https://www.ithaca.xyz/writings/exp-0001)
4. [GitHub: Example `P256Delegation` 7702 contract](https://github.com/paradigmxyz/forge-alphanet/blob/main/src/P256Delegation.sol)
