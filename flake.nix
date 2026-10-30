{
  description = "Polyglot algorithms and data structures study monorepo";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];

      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f (import nixpkgs { inherit system; }));
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            git
          ];
        };

        c = pkgs.mkShell {
          packages =
            with pkgs;
            [
              clang-tools
              gnumake
              pkg-config
            ]
            ++ lib.optionals stdenv.hostPlatform.isLinux [
              gcc
              gdb
              valgrind
            ]
            ++ lib.optionals stdenv.hostPlatform.isDarwin [
              lldb
            ];
        };

        cc = pkgs.mkShell {
          packages =
            with pkgs;
            [
              abseil-cpp
              clang-tools
              cmake
              gnumake
              gtest
              ninja
              pkg-config
            ]
            ++ lib.optionals stdenv.hostPlatform.isLinux [
              gcc
              gdb
              valgrind
            ]
            ++ lib.optionals stdenv.hostPlatform.isDarwin [
              lldb
            ];
        };

        python = pkgs.mkShell {
          packages = with pkgs; [
            uv
            ty
            ruff
            mypy
            pylint
            python315
            pkg-config
            stdenv.cc
          ];
          env =
            {
              UV_PYTHON_PREFERENCE = "only-system";
            }
            // pkgs.lib.optionalAttrs pkgs.stdenv.hostPlatform.isLinux {
              LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (
                with pkgs;
                [
                  stdenv.cc.cc.lib
                  zlib
                ]
              );
            };
        };

        scheme = pkgs.mkShell {
          packages = with pkgs; [
            guile
            chez
            racket
          ];
        };

        ocaml = pkgs.mkShell {
          packages = with pkgs; [
            ocaml
            dune_3
            ocamlPackages.findlib
            ocamlPackages.ocamlformat
            ocamlPackages.utop
            ocamlPackages.ocaml-lsp
            ocamlPackages.ocp-indent
          ];
        };

        haskell = pkgs.mkShell {
          packages = with pkgs; [
            ghc
            cabal-install
            haskell-language-server
            hlint
          ];
        };

        erlang = pkgs.mkShell {
          packages = with pkgs; [
            erlang
            rebar3
            erlang-ls
          ];
        };

        javascript = pkgs.mkShell {
          packages = with pkgs; [
            nodejs
            corepack
            typescript
            typescript-language-server
          ];
        };

        bash = pkgs.mkShell {
          packages = with pkgs; [
            bashInteractive
            shellcheck
            shfmt
          ];
        };
      });
    };
}
