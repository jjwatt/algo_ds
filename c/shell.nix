{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	# inputsFrom = with pkgs; [ pkgconfig autoconf automake gnumake ];
	buildInputs = with pkgs; [
		gcc
		pkgconfig
		autoconf
		automake
		libtool
		gnumake
	];
}
