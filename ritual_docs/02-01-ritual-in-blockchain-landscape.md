> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ritual in the Blockchain Landscape

> Understanding Ritual's place in blockchain evolution

export const Spacer = ({gap}) => <div style={{
  marginTop: `${gap}px`
}}></div>;

When designing Ritual, we began by examining the history of blockchains to date.
Many architectural innovations underpinning Ritual are informed by past work
from historic blockchain networks, modified to support the next-generation use
cases of tomorrow.

<Update label="2009">
  <img width="100px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3c2c368b3e11616c59a794da24f52c6d" data-og-width="342" data-og-height="150" data-path="assets/images/ritual-vs-xyz/early-titans.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=fa55446eac741634296f49cd5d5b9ed4 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=6b2b16ae0aa2a81f8168e28a2881bb40 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=8f2e7d90be1c3363b92f3ad69d76ba22 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=05c284332b64c11bad09aea3d66386c8 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=2cebbec2e5d422dcb1a2ebc6a3e09260 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/early-titans.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=0b6e8c41fab14681c199a97db97a972a 2500w" />

  ### Early Titans

  Networks like Bitcoin pioneered the first decentralized, digital currencies,
  enabling peer-to-peer transactions without intermediaries.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Robust decentralization** powered by proof-of-work
    consensus.

    <Icon icon="minus" iconType="solid" color="red" /> **Basic scripting system** preventing
    any smart applications.

    <Icon icon="minus" iconType="solid" color="red" /> **Low throughput** with long block
    times and prohibitive block size.

    <Icon icon="minus" iconType="solid" color="red" /> **Rigid governance** prohibiting feature upgrades to improve
    developer experience.
  </Card>
</Update>

<Update label="2012">
  <img width="130px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=aef7e5fc1768f77e160f13a0c20d2480" data-og-width="438" data-og-height="150" data-path="assets/images/ritual-vs-xyz/payment-networks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=b7125884bb1422789965f284f210b5d3 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=0edb8f44d29f4ad42a92fd4f41fdf8cd 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=8fb357ef1d959082eea1ed46c78ccff9 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=63711cfba7655deec3dbc4f3e486a164 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=22a85c4db68adc64dd0916acd41bb519 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/payment-networks.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=183049c7930dfe219c817bc5df0beac0 2500w" />

  ### Payment Networks

  Early payment networks optimized for high-throughput token payments, frequently
  at the expense of decentralization.

  <Card>
    <Icon icon="plus" iconType="solid" /> **High throughput**, optimized for payments.

    {" "}

    <Icon icon="minus" iconType="solid" color="red" /> **Limited programmability** to
    favor optimizing for just payment use cases.

    {" "}

    <Icon icon="minus" iconType="solid" color="red" /> **Quorum centralization risks**
    due to selected consensus mechanisms.

    <Icon icon="minus" iconType="solid" color="red" /> **Poor developer experience** because of early, complex smart contract environments.
  </Card>
</Update>

<Update label="2014">
  <img width="75px" noZoom src="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=7fd2f71d9df3f35aa44181c66a78d5cb" data-og-width="246" data-og-height="150" data-path="assets/images/ritual-vs-xyz/programmable-upstarts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=280&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=bc068bc597ff3cddb44492261da660d4 280w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=560&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=0a9b5535af702fa1901768d006e7b1bc 560w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=840&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=02e2aeddf485cf9b6e640390b235354b 840w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=1100&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=e94e2d54e3f8cb3294b6829121f9fe13 1100w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=1650&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=bf6296593e9916c8f93ced394ba0875b 1650w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/programmable-upstarts.png?w=2500&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=b5d22ba4e3ee2d99acb1a61003a121c8 2500w" />

  ### Programmable Upstarts

  Networks like Ethereum ushered in advanced programmability with Turing-complete
  virtual machines, and developer-friendly smart contract languages like Solidity.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Programmable smart contracts** to build early on-chain applications.

    <Icon icon="plus" iconType="solid" /> **Simple developer experience** via Solidity
    and EVM tooling ecosystem.

    <Icon icon="minus" iconType="solid" color="red" /> **Low throughput** with strict
    VM computation constraints.

    <Icon icon="minus" iconType="solid" color="red" /> **Inefficient execution pricing**
    generalizing over unique hardware resources.

    <Icon icon="minus" iconType="solid" color="red" /> **Restrictive state access and growth** with high-cost storage operations.
  </Card>
</Update>

<Update label="2019">
  <img width="175px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=a58012b375fa8e40ca0a5525d3372268" data-og-width="630" data-og-height="150" data-path="assets/images/ritual-vs-xyz/eth-killers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3848a42e13c4bbff1acf3cf4b8182591 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=448c772e974465264b8dbe79c4505a2b 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3109eade21225b6fdfb2a79aa8f22ad6 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=0422dbad5a8cb581f08b8ae40c615723 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=a42ed3a69128a8ba8a9ab231424c9a2d 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/eth-killers.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=324cc615580e44e1fd9af4e7c0a6eaa6 2500w" />

  ### "ETH Killers"

  Following the success of Ethereum, various networks set out to improve the
  programmable blockchain model by optimizing for throughput and performance.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Programmable smart contracts** to build early on-chain applications.

    <Icon icon="plus" iconType="solid" /> **High throughput**, commonly via parallel
    transaction processing.

    <Icon icon="minus" iconType="solid" color="red" /> **Difficult DX** because of non-traditional
    VM designs and EVM-familiarity headwinds.

    <Icon icon="minus" iconType="solid" color="red" /> **Segmented ecosystems** with
    fragmented protocols and user bases.

    <Icon icon="minus" iconType="solid" color="red" /> **High validator requirements**
    creating centralization pressures.

    <Icon icon="minus" iconType="solid" color="red" /> **Poor network stability** as a function of early high throughput explorations.
  </Card>
</Update>

<Update label="2020">
  <img width="75px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=e29ddcd3b3ad2b940179fbb5d83b8fa4" data-og-width="246" data-og-height="150" data-path="assets/images/ritual-vs-xyz/interoperable-networks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=42fb71d27aa886a265255289c84e3322 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=a3e8f7f6571f3559942ab0ddd6a43b0e 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=676bf0233761cc3099cfa081d1740b02 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=782ab545346dd759f00895e36e042155 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=8f816f8b028f3b2b8dde089d2c99b9c3 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/interoperable-networks.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=c772aa16540d64906142ba59c89315cf 2500w" />

  ### Interoperable Networks

  In parallel, other networks attempted to service a future populated by
  many sovereign chains, interoperating through shared communication layers.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Modular, shared security** for quick network
    bootstrapping.

    <Icon icon="minus" iconType="solid" color="red" /> **Poor cross-chain UX** forcing
    users to segment activity.

    <Icon icon="minus" iconType="solid" color="red" /> **Liquidity fragmentation** with
    separated capital pockets.

    <Icon icon="minus" iconType="solid" color="red" /> **High security risk** with network-by-network
    validator security intricacies.

    <Icon icon="minus" iconType="solid" color="red" /> **High operational complexity** for node operators and developers alike.
  </Card>
</Update>

<Update label="2021">
  <img width="105px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=aa898a87dbb540cd8adb7878e862f716" data-og-width="342" data-og-height="150" data-path="assets/images/ritual-vs-xyz/l2-networks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=0c3affeebbcc2123f3c34cc458c188fa 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=863e3ea2a6fdc6efd918d3f6c98e6144 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=06e19dfbb12cea95f59e5e3bb1c1f689 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=0c4a5a59e80ae9369ec6bca09d87261e 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=7673705987d64ee76e31743cf7f983ad 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/l2-networks.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=3855a8db3c53c48cab50d2f20f5df4fa 2500w" />

  ### Layer-2 Networks

  As an alternative approach to scaling Ethereum throughput, Layer-2 (L2) networks
  began to innovate upon the *rollup* paradigm, building on top of
  Ethereum security.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Low operational complexity** for deployment
    and maintenance ease.

    <Icon icon="plus" iconType="solid" /> **Familiar experience** for existing Ethereum-adjacent
    users and developers.

    <Icon icon="minus" iconType="solid" color="red" /> **Liquidity fragmentation** across
    L2 network ecosystem.

    <Icon icon="minus" iconType="solid" color="red" /> **Centralization risks** via single
    sequencers and whitelisted state root proposers.

    <Icon icon="minus" iconType="solid" color="red" /> **Inefficient execution pricing**
    with rudimentary MEV environments and inherited Ethereum execution pricing downfalls.
  </Card>
</Update>

<Update label="2023">
  <img width="75px" noZoom src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=879a064e7f46800268dbe071adacb326" data-og-width="246" data-og-height="150" data-path="assets/images/ritual-vs-xyz/modern-scalers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=00766bbaace2db24663c42b275fba76d 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=45576664f07b36aa7d79008950e2de8d 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=f4e8e80533bd14751697d6cd2a0c6e94 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=92e0a9edb71a5d6b31c26e261989a8f9 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=5e5882e7bc110cb0e5d309af80d4353f 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/ritual-vs-xyz/modern-scalers.png?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=dcc7a239f7b942b4a89b772323ba3878 2500w" />

  ### Modern Scalers

  Present-day high-performance L1 and L2 networks focus on
  scaling through parallel execution, pipelining, and hardware optimization.

  <Card>
    <Icon icon="plus" iconType="solid" /> **High throughput** through software and hardware
    optimization.

    <Icon icon="plus" iconType="solid" /> **Parallel VM execution** to support smart
    contract scaling.

    <Icon icon="minus" iconType="solid" color="red" /> **Overfit optimization** for traditional
    blockchain workloads.

    <Icon icon="minus" iconType="solid" color="red" /> **High, uniform validator requirements**
    prohibiting average participants, with increased centralization risks.
  </Card>
</Update>

<Update label="2025++">
  <img width="45px" noZoom src="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=6f00a4f1aaa6996961b740760b938b47" data-og-width="150" data-og-height="150" data-path="assets/images/ritual-vs-xyz/ritual.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=280&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=748cc7a619b6a8dfd7b6631254a1c1b2 280w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=560&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=8e58970ea45ceb3d4306a179900be6da 560w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=840&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=1ebe843b3d9071c034db8ab799426dd4 840w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=1100&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=f875d0417f035b976a1ffc674443b184 1100w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=1650&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=95f136c61f9c59f91638b3bf9cafe39e 1650w, https://mintcdn.com/ritualfoundation/sxqQxm2wyqht7Z65/assets/images/ritual-vs-xyz/ritual.png?w=2500&fit=max&auto=format&n=sxqQxm2wyqht7Z65&q=85&s=43f00c1479948ff54ff9793d4c316a5f 2500w" />

  ### Ritual

  Ritual moves beyond scaling existing workloads to fundamentally re-imagine
  on-chain computation and enrich user functionality.

  <Card>
    <Icon icon="plus" iconType="solid" /> **Native, heterogeneous compute** with support
    for AI Inference, ZK Proving & Verification, TEE execution, and future paradigms
    via forward-compatible architecture.

    <Icon icon="plus" iconType="solid" /> **Flexible verification** with modular computational
    primitives.

    <Icon icon="plus" iconType="solid" /> **Node specialization** enabling diverse participants
    and workload specialization.

    <Icon icon="plus" iconType="solid" /> **State-of-the-art execution pricing** via a novel fee market
    design: Resonance.
  </Card>
</Update>
