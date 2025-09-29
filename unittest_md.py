import sys, unittest
from md import calcenergy

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        from ase.lattice.cubic import FaceCenteredCubic, BodyCenteredCubic
        from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
        from asap3 import EMT

        size = 10
        atoms = FaceCenteredCubic(
            directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            symbol='Cu',
            size=(size, size, size),
            pbc=True,
        )

        # Describe the interatomic interactions with the Effective Medium Theory
        atoms.calc = EMT()

        # Set the momenta corresponding to T=300K
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)

        epot, ekin, temp, etot = calcenergy(atoms)

        self.assertTrue( abs(ekin) < 0.5 )
        self.assertTrue( temp < 310 and temp > 290)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())


