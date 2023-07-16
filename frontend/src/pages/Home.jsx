import {Button, Container} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import { useParams } from 'react-router-dom';

const Home = () => {
  const {user_id} = useParams();
  const defaultUserId = 10;
    return (
        <div className="App">
          <header className="App-header">
            <h1 className='mb-4'>Welcome to Yodu Tournament</h1>
            <Container className="d-flex justify-content-center">
              <Button variant="warning" className="mx-2">
                <Link to="/recommended_tournament" className='link-text'>Show All Tournament</Link>
              </Button>
              <Button variant="warning" className='mx-2'>
                <Link to={`/recommended_tournament/${user_id || defaultUserId}`} className='link-text'>Show Tournament by User ID</Link>
              </Button>
              <Button variant="warning" className='mx-2'>
                <Link to="/join_tournament/1/1" className='link-text'>
                  Join Tournament
                </Link>
              </Button>
            </Container>
          </header>
      </div>
    );
}

export default Home;