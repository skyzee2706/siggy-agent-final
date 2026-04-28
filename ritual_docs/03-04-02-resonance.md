> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Resonance

> Resonance is a state-of-the-art transaction fee mechanism to efficiently match supply and demand, offering users optimally priced transaction execution.

<Info>
  To read in-depth about Resonance architecture, reference the [architecture
  page](/architecture/resonance).
</Info>

<Frame>
  <video src="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/videos/resonance.mp4?fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=0256115bcccd0dcf0a794b562d3b2d0f" autoPlay controls disablePictureInPicture loop playsInline muted preload="auto" data-path="assets/videos/resonance.mp4" />
</Frame>

***

## Heterogeneous blockchains

Blockchain transactions have become **increasingly heterogeneous**:

<Note>
  Heterogeneous in this context means increasingly complex and different or
  *unique* in nature.
</Note>

* **Bitcoin** supported only simple arithmetic operations (e.g. transfers)
* **Ethereum** introduced smart contracts, enabling transactions to execute
  arbitrary logic
* **Blobs (EIP-4844)** introduced transactions to store blobs of data on
  Ethereum
* **Solana, Monad, and MegaETH** introduce parallel transaction execution

As we move forward, transaction heterogeneity **will grow exponentially** as new
applications (e.g. gaming or AI) bring more complex computation on-chain.

<Frame caption="Transaction heterogeneity grows exponentially.">
  <img src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=806e42099acf39beccd6ba6ef82f8559" alt="Past, Present, & Future of Blockchain Execution Heterogeneity" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="assets/images/broker-timeline.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=8dd674876d606ee95d5211491300ff50 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=8f2593369256bb929213560b0dafc1b2 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ee279f70978b1829ab0f33a1228c8e57 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ae5c452ecfcd3a748a66f241c5d6ad46 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=b31e2c99b9a8c900f67e6083333ef4d0 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-timeline.webp?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=49b6b0c053cc16638bf42de91a4f8f0c 2500w" />
</Frame>

***

## Existing fee mechanisms are insufficient

As we scale the paradigm of what is possible with blockchain transactions, we
start to see that existing fee mechanisms are insufficient in supporting this
heterogeneity.

<Note>
  A fee mechanism is a mechanism by which blockchains price execution of
  transactions. The simplest mechanism is a **first-price auction**, akin to a
  bidding war, where transactions that pay the highest fees, irrespective of
  what they are executing, are included.
</Note>

The leading mechanism for handling these heterogeneous transactions today is
[multi-dimensional EIP-1559](https://vitalik.eth.limo/general/2024/05/09/multidim.html).
In [section A of our formal paper](https://arxiv.org/abs/2411.11789), we show
that this mechanism:

1. Suffers from poor welfare guarantees as the number of dimensions (aka degree
   of heterogeneity) increases
2. Requires the hardcoding of the set of resources into the protocol, which can
   only be updated via hard forks
3. Faces information-theoretic challenges in setting the right base fees across
   many dimensions

For users, practically, this means:

<CardGroup cols={2}>
  <Card title="Increased Costs" icon="money-bill-trend-up">
    Complex transactions become expensive as the mechanism fails to price them efficiently
  </Card>

  <Card title="Limited Support" icon="puzzle-piece-simple">
    New transaction types that are not hard-coded into the protocol are unsupported
  </Card>

  <Card title="Pricing Complexity" icon="calculator">
    Users struggle to set appropriate fees when transactions involve complex
    execution logic
  </Card>

  <Card title="Failed Execution" icon="triangle-exclamation">
    Transactions fail when the fee mechanism cannot efficiently scale to meet demand
  </Card>
</CardGroup>

***

## Resonance is the answer

Resonance is a new, state-of-the-art fee mechanism built for heterogeneous
compute with a two-sided market setting (matching users to nodes).

### Resonance for users

1. Each transaction specifies a `valuation` it wants to pay for execution
2. Transactions can be executed by single nodes or multiple nodes
3. Users can **choose to prioritize speed or cost** when submitting transactions
4. Users can execute **any type of compute**, without protocol-level constraints
5. Transactions can execute **privately** via multi-party assignment

### Resonance for nodes

1. Nodes specify a `cost function` for each transaction, granularly dictating
   execution costs
2. Nodes can **specialize** in specific types of compute, e.g. AI inference
3. Nodes can execute **any type of compute**, without protocol-level constraints
4. Nodes can execute unconflicting transactions **in parallel**

### Resonance for the network

1. Transactions are efficiently matched, **optimizing for both cost and speed**
2. Node capacity is **optimally allocated**
3. Users have **full preference** over transaction execution
4. With [Symphony](/whats-new/symphony), parts of the network can be specialized

Our unique fee mechanism optimizes for the **optimal and efficient matching** of
transactions to nodes, ensuring that all parties in the system are better-off
for using the mechanism truthfully.

***

## Brokers

Under the hood, Resonance works by introducing a new entity known as a
**broker**. Brokers are sophisticated, profit-seeking agents that compute
matchings between transactions and nodes.

<Note>
  Consider the parallel to brokers as block builders or MEV searchers: advanced
  participants that use their informed priors to efficiently match transactions,
  pocketing the spread between transaction `valuation` and node execution `cost`
  in the process.
</Note>

<Tip>
  The properties of the Resonance mechanism ensure that brokers—who are
  responsible for matching transactions—behave predictably and fairly. This is a
  level of reliability that Ethereum's current block-building process doesn't
  fully guarantee.
</Tip>

***

## Future work

We plan to extend Resonance in several key areas to hyperscale modern apps and
protocol usage:

1. Scheduled transactions can be natively priced to enable use cases like agents
   on-chain to be economically efficient
2. No need to trust Ritual anymore for running the auctioneer: anyone can run it
3. Increased TPS for heterogeneous transactions priced via Resonance as we allow
   for streaming settings
4. Research into posted price mechanisms to enable users to have an experience
   similar to Uber for pricing transactions

***

## Further reading

For more information on Ritual’s fee mechanism, see our blog posts and academic
paper:

<CardGroup cols={2}>
  <Card title="Resonance: A Market Mechanism for Heterogeneous Computation" img="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=9dfd667ddf30d91675c4b03be45ae64e" icon="link" href="https://ritual.net/blog/resonance-pt1" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="assets/images/broker-heterogeneous.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=a4e17c979e9da692d5663e95cff1def4 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=4627f0a3cb6f2b3acfa9653d5580f18c 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3bff0e38c21a783a90bf81cfea50e910 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ec82f5d3df1ea83bae1f3ab647ae358b 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=64408038a416572d9570bb92b2416d7a 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-heterogeneous.webp?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=9baa14e80cf8592b8f179122ed60262f 2500w">
    Resonance enables heterogeneous computation on-chain. This post builds
    towards a formal definition of the heterogeneous setting.
  </Card>

  <Card title="The Resonance Mechanism and its Properties" img="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=2f74d5c45221cd8167f8985e5edb744b" icon="link" href="https://ritual.net/blog/resonance-pt2" data-og-width="2400" width="2400" data-og-height="1350" height="1350" data-path="assets/images/broker-quadrant.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=9c3c2ec89acc0dedfe62cf5208c05a8c 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ef222f2e1cf9f7ae013cf872c4503a16 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=dd17b0449ac7d829d69d3c98b3e88258 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=025e6f322b01ae0df7dc300feb949c22 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=9afb62f48c741f63603922566f418dfe 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/broker-quadrant.webp?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=ef6402db651d1e9f83b2f8788c239c73 2500w">
    This post gives a formal description of the Resonance mechanism and the
    desiderata it satisfies.
  </Card>

  <Card title="arXiv: Resonance: Transaction Fees for Heterogeneous Computation" img="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=18542238fa3329375ba86572e65f3179" icon="link" href="https://arxiv.org/abs/2411.11789" data-og-width="1200" width="1200" data-og-height="678" height="678" data-path="assets/images/resonance-arxiv-meta.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=020b0a6fc6fa9b6eef12cf0be5e0eb8f 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=e3d17430730a3238ff75d4f1180ad9cb 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=d567a23a9084bdc1e5fd234bc46b70bb 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=076198bdf9268bf5e325559e0cc7a8c9 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=57124fb1caaeecacfeb30051566e94e4 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/resonance-arxiv-meta.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=4e54de75bc73f84b5a9a6d3d8e085fa9 2500w">
    This paper introduces Resonance: a new kind of transaction fee mechanism for
    the general two-sided market setting (with users on one side and nodes on
    the other), where both sides of the market exhibit a high degree of
    heterogeneity.
  </Card>
</CardGroup>
