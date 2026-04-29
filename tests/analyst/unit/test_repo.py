from app.agents.analyst.repository import AnalystRepository
import pytest
from sqlmodel import SQLModel, create_engine, Session
from app.agents.analyst.models import Analysis


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture
def analyst_repository(session):
    return AnalystRepository(db=session)

def test_create_analysis(analyst_repository):
    analysis = Analysis(
        topic=["Test Topic"],
        input="Test Input",
        fixture_id=1,
        session_id=1,
        output="Test Output",
        status="pending"
    )
    created = analyst_repository.create(analysis)
    assert created.id is not None, "Saved analysis should have an ID assigned"
    
def test_update_analysis(analyst_repository, session):
    analysis = Analysis(
        topic=["Test Topic"],
        input="Test Input",
        status="pending"
    )
    session.add(analysis)
    session.commit()
    session.refresh(analysis)

    analysis.topic = ["Updated Topic"]
    updated = analyst_repository.update(analysis)

    assert updated.topic == ["Updated Topic"], "Topic should reflect the update"


def test_delete_analysis(analyst_repository, session): 
    analysis = Analysis(
        topic=["test topic"],
        input="Test Input",
        fixture_id=1,
        session_id=1,
        output="Test Output",
        status="pending"
    )
    session.add(analysis)
    session.commit()
    session.refresh(analysis)
    
    analyst_repository.delete(analysis.id)

    assert analyst_repository.get_by_id(analysis.id) is None 


    
    
def test_get_by_id(analyst_repository, session):
    analysis = Analysis(
        topic=["Test Topic"],
        input="Test Input",
        status="pending"
    )
    session.add(analysis)
    session.commit()
    session.refresh(analysis)

    result = analyst_repository.get_by_id(analysis.id)
    assert result is not None, "Should return an analysis for existing ID"
    assert result.id == analysis.id
    


def test_get_by_topic(analyst_repository, session):
    analysis = Analysis(
        topic=["Test Topic"],
        input="Test Input",
        fixture_id=1,
        session_id=1,
        output="Test Output",
        status="pending"
    )
    session.add(analysis)
    session.commit()
    session.refresh(analysis)

    result = analyst_repository.get_by_topic("Test Topic")
    assert len(result) == 1, "should return an analysis"
    assert result[0].topic == ["Test Topic"]


def test_by_player(analyst_repository, session):
    analysis = Analysis(
        topic=["Test Topic"],
        input="Test Input",
        player_name="Harry Kane",
        fixture_id=1,
        session_id=1,
        output="Test Output",
        status="pending"
    )
    session.add(analysis)
    session.commit()
    session.refresh(analysis)

    result = analyst_repository.get_by_player("Harry Kane")
    assert len(result) == 1, "Should return one matching analysis"
    assert result[0].player_name == "Harry Kane"
    
