from typing_extensions import Self

from sympy import Basic
from sympy.stats.drv import SingleDiscreteDistribution
from sympy.stats.rv import RandomSymbol

__all__ = ["FlorySchulz", "Geometric", "Hermite", "Logarithmic", "NegativeBinomial", "Poisson", "Skellam", "YuleSimon", "Zeta"]

def rv(symbol, cls, *args, **kwargs) -> RandomSymbol: ...

class DiscreteDistributionHandmade(SingleDiscreteDistribution):
    _argnames = ...
    def __new__(cls, pdf, set=...) -> Self: ...
    @property
    def set(self) -> Basic: ...
    @staticmethod
    def check(pdf, set) -> None: ...

def DiscreteRV(symbol, density, set=..., **kwargs) -> RandomSymbol: ...

class FlorySchulzDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a) -> None: ...
    def pdf(self, k): ...

def FlorySchulz(name, a) -> RandomSymbol: ...

class GeometricDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(p) -> None: ...
    def pdf(self, k): ...

def Geometric(name, p) -> RandomSymbol: ...

class HermiteDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a1, a2) -> None: ...
    def pdf(self, k): ...

def Hermite(name, a1, a2) -> RandomSymbol: ...

class LogarithmicDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(p) -> None: ...
    def pdf(self, k): ...

def Logarithmic(name, p) -> RandomSymbol: ...

class NegativeBinomialDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(r, p) -> None: ...
    def pdf(self, k): ...

def NegativeBinomial(name, r, p) -> RandomSymbol: ...

class PoissonDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(lamda) -> None: ...
    def pdf(self, k): ...

def Poisson(name, lamda) -> RandomSymbol: ...

class SkellamDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu1, mu2) -> None: ...
    def pdf(self, k): ...

def Skellam(name, mu1, mu2) -> RandomSymbol: ...

class YuleSimonDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(rho) -> None: ...
    def pdf(self, k): ...

def YuleSimon(name, rho) -> RandomSymbol: ...

class ZetaDistribution(SingleDiscreteDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(s) -> None: ...
    def pdf(self, k): ...

def Zeta(name, s) -> RandomSymbol: ...