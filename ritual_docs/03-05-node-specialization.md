> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Node specialization

## Background

Traditional blockchains like Ethereum operate by coming to consensus over
ordering and replicated execution of transactions. Step-by-step, it looks
something like:

<Steps>
  <Step title="Block proposer elected">
    A *leader*, more commonly referred to as a *block proposer*, is elected to
    extend the chain by proposing a block (today, via stake-weighted
    pseudo-random selection).

    This block proposer collects transactions from both public and private transaction pools (using by running a sidecar like [mev-boost](https://writings.flashbots.net/beginners-guide-mevboost)), builds a valid block according to protocol rules, and broadcasts it to the rest of the network.
  </Step>

  <Step title="Validator re-execution">
    Next, all validators in the network receive the new head block from the block proposer and **re-execute** the block locally, via their execution clients, to determine block validity.

    Today, in Ethereum ([via the official specification](https://github.com/ethereum/devp2p/blob/master/caps/eth.md#block-encoding-and-validity)), this involves asserting:

    1. A block `header` is valid
    2. All `transaction`(s) are valid by their [validity rules](https://github.com/ethereum/devp2p/blob/master/caps/eth.md#transaction-encoding-and-validity)
    3. The sum of transaction `gasLimit`(s) do not exceed the block `gasLimit`
    4. **A block's `stateRoot` matches a local `stateRoot` after executing all transactions**
    5. ...and similar `txsRoot`, `withdrawalsHash`, `ommersHash`, and other checks

    Notice, in step 4, that Ethereum validators, irrespective of their hardware or specifications, must be capable of executing **all** Ethereum transactions.
  </Step>

  <Step title="Achieving consensus">
    Finally, validators that have re-executed and asserted validity of a new head block publish their votes in favour of the block.

    Via the [fork choice rule](https://eth2book.info/capella/part2/consensus/preliminaries/#fork-choice-rules), all correct nodes eventually agree on a common view of the canonical chain, finalizing a block to Ethereum state.
  </Step>
</Steps>

### Limitations

Today, the
[Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/) is
purposefully limited in the types, computational complexity, and cost of
operations it supports.

In part, this is because of a conflict in Ethereum's architecture demanding
*each node execute all transactions*, yet
[prohibitively low](https://ethereum.org/en/developers/docs/nodes-and-clients/run-a-node/#requirements)
minimum requirements to run a node, optimized for the long-tail of residential
validators.

Commonly, proposals to improve chain performance or enable net-new user
functionality are met with pushback to preserve the minimum requirements.

Namely, this results in:

1. Only supporting limited, homogeneous computation optimized for the weakest
   node
2. Best-case chain performance dependent on worst-case node performance
3. No user preference over compute execution; all nodes paid the same
   irrespective of hardware, capabilities, or performance

## Optimized Architecture

Ritual Chain introduces **node specialization** through architecture
purpose-built for reducing redundant re-execution and enabling user preference:

<Steps>
  <Step title="Symphony reduces replicated execution">
    Symphony is a new consensus protocol leveraging dual proof sharding, distributed verification, and optimal sampling to reduce replicated execution.

    At core, the principle behind Symphony is to **execute-once-verify-many-times**. Single nodes are selected for transaction execution (via [Resonance](/whats-new/resonance)). In addition to generating execution outputs, these nodes also generate succinct computation proofs.

    In place of transaction re-execution by all validators, subsets of nodes now verify succinct proofs and broadcast transaction validity, with the network collectively reaching execution consensus.

    **Via Symphony, re-execution is made redundant, with nodes free to service *just* their specialized computation, while still participating in validating the network.**

    <Card title="Symphony" icon="link" href="/whats-new/symphony">
      Read more about Symphony—Ritual's new consensus protocol.
    </Card>
  </Step>

  <Step title="Resonance enables user preference">
    Resonance is a new, state-of-the-art fee mechanism built for heterogeneous compute.

    Traditional blockchains like Ethereum:

    1. Inefficiently price unique resources (computation, storage, etc.) as identical
    2. Force users to pay fees subsidizing transaction re-execution across all nodes
    3. Limit users from expressing their execution preferences

    Resonance is a two-sided marketplace to match heterogeneous transactions to heterogeneous nodes.

    **Via Resonance, users can express their preferences to prioritize cost or speed, with transactions efficiently matched to specialized execution nodes.**

    <Card title="Resonance" icon="link" href="/whats-new/resonance">
      Read more about Resonance—Ritual's state-of-the-art fee market design.
    </Card>
  </Step>
</Steps>

### Benefits

Via this architecture, Ritual Chain is the **most expressive blockchain in
existence**, built to meet the demands of complex on-chain applications and
enable net-new user functionality:

1. Node specialization optimizes network performance, allowing for smoother,
   more tailored processing across different workloads.
2. Nodes are rewarded based on their unique computational strengths, creating a
   diverse ecosystem that incentivizes both high-performance and
   resource-constrained participants to join and contribute effectively.
3. Users gain flexibility, with options to prioritize cost or speed based on
   their preferences.
