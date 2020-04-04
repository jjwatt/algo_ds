# simple python shell to get started
with import <nixpkgs> {};
(python37.withPackages (ps: [ps.ipython ps.ipdb])).env
