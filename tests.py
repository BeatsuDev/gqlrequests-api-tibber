from gqlrequests.query import Query

from gqlrequests_api_tibber import RootQuery


def test_viewer():
    query = Query(RootQuery, indents=2)

    with open("queries/viewer.graphql", "r") as file:
        assert str(query) == file.read()
