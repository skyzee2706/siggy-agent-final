> ## Documentation Index
> Fetch the complete documentation index at: https://ritualfoundation.org/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execution Sidecars

> Underlying our expressive compute precompiles—which enable any type of heterogeneous compute, including [AI inference](/whats-new/evm++-sidecars/ai-inference/classical-ml-inference), [ZK proof verification](/whats-new/evm++-sidecars/zk-proving-and-verification), [TEE code execution](/whats-new/evm++-sidecars/tee-execution), and beyond—are our optimized execution sidecars.

<Frame caption="Ritual Chain features two sets of precompiles: (1) native precompiles implemented as EIP extensions directly into the execution client and (2) heterogeneous compute precompiles, implemented via optimized execution sidecars exposed through the EVM precompile interface.">
  <img src="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=bc6ee4ee56d06cc7647cb62b6ba5b748" alt="Sidecars diagram" data-og-width="1200" width="1200" data-og-height="675" height="675" data-path="assets/images/precompiles.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=280&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=df769b41c629272a17a1682c97471174 280w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=560&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=745ddead206efbfbfa0024d56b0ff900 560w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=840&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=41a47380f6f3659405c2d783c45f8682 840w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=1100&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=6006e7817ef6b12706047016961ef36d 1100w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=1650&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=1e782a14a0d0e023e0e15a13ad33f46f 1650w, https://mintcdn.com/ritualfoundation/a7GImEbJRnhEjeNO/assets/images/precompiles.svg?w=2500&fit=max&auto=format&n=a7GImEbJRnhEjeNO&q=85&s=4de19cc253cf3deeb732f07f327d14f0 2500w" />
</Frame>

These sidecars run and scale parallel to the Ritual execution client, invoked
through abstraction via the EVM precompile interface. By default, these sidecars
are purpose-built for execution and proof generation avoiding
blockchain-specific overhead, run as an isolated process or remote to an
execution client, and can be selectively enabled by node operators based on
their available infrastructure, underlying hardware, or firewalled preferences.

Because of their generic architecture, sidecars enable Ritual to easily service
heterogeneous compute across any supported execution environment by connecting
to their precompile-like interfaces (EVM precompiles, SVM precompiled programs,
MoveVM system modules, etc.).

## Looking forward

Sidecars today are stateless, but will soon be extended to being stateful,
allowing for a minimally invasive approach to enabling asynchronous execution on
our chain for long-running compute precompiles.
