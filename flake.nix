{
  description = "A simple python dev template";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };
  outputs = {
    self,
    nixpkgs,
  }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    python = pkgs.python310.withPackages (p:
      with p; [
        hydra-core
      ]);
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [python pkgs.python3];
    };
  };
}
