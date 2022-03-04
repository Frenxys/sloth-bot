import os
import sys

import pytest
from unittest.mock import Mock
from typing import List, Dict, Union, Optional, Any

from .conftest import (
    DatabaseDriver,
    Query,
    Result,
    get_users,
    _INSERT,
    createConnection,
    DiscordMember
)
from contextlib import suppress

DNK_ID: int = 647452832852869120

# SLC: Sloth Language Class
# RUN: pytest --asyncio-mode=auto --capture=no

class TestSlothLanguageClass:
    """ Class for testing the features inside Sloth's
    Language Class system. """

    def setup(self) -> None:
        """ Setup of the test class, which creates a database connection, cache etc. """

        cursor, connection = createConnection()

        refer = DatabaseDriver.execute

        def execute(self: DatabaseDriver, query: Union[str, Query]) -> Result:
            """ Executes a query using the database driver. """

            print("execute", query)

            assert isinstance(query, Query), \
                "Unexpected raw query execution"

            result = refer(self, query)

            if query.kind == _INSERT and result.commited:
                model = result.asdict()

            return result

        DatabaseDriver.execute = execute
        self.driver = DatabaseDriver(cursor, connection)

        self.users: List[Dict[str, Any]] = get_users()

    def get_user(
        self,
        user_id: int,
    ) -> Optional[DiscordMember]:
        """ Gets a vendor for the product creation.
        :param vendor: The vendor to get. """

        with suppress(Exception):
            return next(x
                for x in self.users
                if x["id"] == user_id)
        return

    # @pytest.mark.skip(reason="Not implemented.")
    @pytest.mark.asyncio
    async def test_start_classroom(self) -> None:
        """ Tests the creation of a classroom. """


        from cogs import teacherfeedback
        print(self.get_user(user_id=DNK_ID))
        # dnk = self.users
        # teacherfeedback.TeacherFeedback.create_class(member)
        
        #  = Mock()


    @pytest.mark.skip(reason="Not implemented.")
    def test_end_classroom(self) -> None: pass

    @pytest.mark.skip(reason="Not implemented.")
    def test_reward_people(self) -> None: pass
