# amd-cpu-pm
Scripts to manage AMD CPU

## Requirements:
* amd-pstate to be enabled

## Dependencies: 
* power profiles daemon
* python3

## Commands:
* `-c`, `--cpu`: Sets cpu EPP. Available options: `power` `balance_power` `balance_performance` `performance`
* `-p`, `--platform`: Sets platform power profile. Available options: `power-saver` `balanced` `performance`
* `-g`,  `--gpu`:Sets igpu and dgpu(if available) profile. Available options: `low` `auto` `high`

  Example: `cpuctl --cpu balance_power --platform power-saver --gpu auto`

