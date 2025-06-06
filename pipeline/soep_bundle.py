from dataclasses import dataclass
import pandas as pd
from loaders.registry import LoaderRegistry

@dataclass
class SOEPDataBundle:
    ppath: pd.DataFrame
    pl: pd.DataFrame
    phrf: pd.DataFrame
    pgen: pd.DataFrame
    pkal: pd.DataFrame 
    region: pd.DataFrame
    hgen: pd.DataFrame
    bioparen: pd.DataFrame
    biol: pd.DataFrame
    biosib: pd.DataFrame 
    pwealth: pd.DataFrame

    @classmethod
    def from_registry(cls, registry: LoaderRegistry) -> "SOEPDataBundle":
        return cls(
            ppath=registry.ppath(),
            region=registry.region(),
            hgen=registry.hgen(),
            bioparen=registry.bioparen(),
            biol=registry.biol(),
            pl=registry.pl(),
            pgen=registry.pgen(),
            biosib=registry.biosib(),
            pkal=registry.pkal(),
            pwealth=registry.pwealth(),
            phrf=registry.phrf()
        )
