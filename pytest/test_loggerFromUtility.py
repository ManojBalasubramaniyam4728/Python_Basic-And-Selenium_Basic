import pytest

from BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestDemo1(BaseClass):
     def test_Login(self, dataLoad):
         log=self.getLogger()
         log.info(dataLoad)
         log.info(dataLoad[1])
         log.info(dataLoad[2])