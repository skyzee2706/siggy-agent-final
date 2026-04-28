> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Transactions

> Scheduled transactions enable recurring, conditional invocation of smart contract functions, at the top of a block, without the need for external keepers.

<Frame>
  <video src="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/videos/scheduling.mp4?fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=47dd0661c6f340863f92f44c8f7e368f" autoPlay controls disablePictureInPicture loop playsInline muted preload="auto" data-path="assets/videos/scheduling.mp4" />
</Frame>

## Homogenous compute

We introduce a new predeploy contract, `Scheduler`. This minimal contract,
callable only by other smart contracts (including
[EIP-7702](/whats-new/evm++/account-abstraction) delegated addresses), maintains
state of `ScheduledCall`(s) and escrows future transaction fees.

Developers can easily set up scheduled smart contract invocations through
`Scheduler.schedule()`, which takes as inputs details about an invocated
function and calldata, invocation frequency, an optional conditional execution
function (returning `True/False`), and fee limit preferences. Developers can
cancel future invocations and receive remaining escrowed balance refund via
`Scheduler.cancel()`.

Next, we extend the standard Ethereum block-building process. Block producers
maintain the latest state of `ScheduledCall`(s) from the `Scheduler`. During
intervals when a `ScheduledCall` should be executed, nodes include a `SystemTx`
transaction
([akin to L2 networks like Optimism](https://github.com/ethereum-optimism/op-geth/blob/647c346e2bef36219cc7b47d76b1cb87e7ca29e4/core/types/transaction.go#L99))
invoking a developer smart contract at the top of their produced block,
conditional on transaction validity and sufficient fees. To developer smart
contracts, this transaction acts as any other invocation, except with a
`msg.sender` equal to a constant `SystemTxAccount`.

## Heterogeneous compute

Scheduled transactions containing heterogeneous compute consume the same,
standard `Scheduler` interface, but are executed via the
[Resonance fee mechanism](/architecture/resonance).

Today, we hijack the mechanism by just-in-time pricing each invocation of a
`ScheduledCall` as if it were an independent, unscheduled transaction. Brokers
are given a one-block heads-up to upcoming scheduled transactions that they can
include in future allocations. These transactions are executed by assigned
subsets of the network with outputs and proofs gossiped to block producers for
inclusion in similar fashion to the homogenous case.

## Top-of-block inclusion

Uniquely, scheduled transactions have privileged inclusion at top-of-block.

This enables priority execution for critical, automated operations like oracle
updates and rebalancing mechanisms, with separately priced fee markets.

<Card title="Enshrined oracles: scheduled transactions" icon="crystal-ball" href="/whats-new/enshrined-oracles/scheduled-transactions" horizontal>
  Learn more about enabling enshrined oracles through scheduled transactions.
</Card>

## Looking forward

We expect to:

* Extend [Resonance](/architecture/resonance) to support natively pricing
  scheduled transactions within the mechanism itself. This will:
  * Reduce end-to-end time to transaction finality given the mechanism will not
    be eagerly triggered at each independent iteration of a `ScheduledCall`
  * Enable more robust execution pricing by accounting for `ScheduledCall`
    invocations as continual, predictable, yet cancellable, future execution
    rather than disjoint events
* Embrace true PBS++
  ([proposer-builder separation](https://ethereum.org/en/roadmap/pbs/)) by
  enabling brokers to account for the preferential treatment given to scheduled
  transactions as it relates to top-of-block inclusion during block construction
