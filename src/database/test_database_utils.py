import unittest
from unittest.mock import MagicMock, patch
from sqlalchemy import Table
from database_utils import get_connection, process_group


class TestDatabaseUtils(unittest.TestCase):
    """Test database utils"""

    @patch("sqlalchemy.create_engine")
    def test_get_connection(self, mock_create_engine):
        db_user = "test_user"
        db_password = "test_password"
        db_host = "test_host"
        db_name = "test_db"

        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        connection = get_connection(db_user, db_password, db_host, db_name)

        mock_create_engine.assert_called_once_with(
            f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
        )

        self.assertEqual(connection, mock_engine.connect.return_value)

    @patch("sqlalchemy.create_engine")
    def test_process_group(self, mock_create_engine):
        mock_connection = MagicMock()
        mock_engine = MagicMock()
        mock_table = MagicMock(spec=Table)

        mock_create_engine.return_value.connect.return_value = mock_connection

        mock_execute = MagicMock()
        mock_connection.execute = mock_execute

        group_data = [
            (
                "Will",
                "Smith",
                "123 Main St",
                "will@example.com",
                "1234567890",
                "2000-01-01",
                "Engineer",
                "ABC Inc",
                "USA",
                "New York",
            ),
        ]

        process_group(mock_engine, mock_table, group_data)
        expected_calls = [
            MagicMock(name="insert_statement", insert=MagicMock())
            for _ in range(len(group_data))
        ]
        mock_table.insert.assert_has_calls(expected_calls, any_order=True)

        self.assertEqual(mock_execute.call_count, len(group_data))

        mock_connection.begin.assert_called_once()
        mock_connection.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
