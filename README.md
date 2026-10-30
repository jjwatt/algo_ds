# algo_ds

Polyglot monorepo for Algorithms and Data Structures studying and practice.

I find studying and writing the same algorithms in different languages and styles immensely helpful for learning.

## Layout

- Language directories (`bash/`, `c/`, `cc/`, `erlang/`, `haskell/`, `ocaml/`, `python/`, `scheme/`), each configured with its own `.envrc` pointing to the corresponding `devShell` in [`flake.nix`](flake.nix).
- `references/`: Third-party algorithm & textbook repositories tracked as git submodules.
- `tadm.org`: Notes and exercises from *The Algorithm Design Manual*.
