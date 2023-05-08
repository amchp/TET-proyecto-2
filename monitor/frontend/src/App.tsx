import './App.css';
import ClientList from './components/ClientList';
import Footer from './components/Footer';
import Header from './components/Header';


function App() {
    return (
        <div className="w-full h-screen">
            <div className="w-full h-screen flex flex-col bg-gradient-to-r from-gray-900/95  to-dark-blue-900/95">
                <header className="z-10">
                    <Header />
                </header>
                <main className="w-full px-8 h-full flex overflow-hidden justify-center max-w-screen-xl mx-auto">
                    <div className='w-full overflow-y-auto scrollbar-hide'>
                        <ClientList />
                    </div>
                </main>
                <footer>
                    <Footer />
                </footer>
            </div>
        </div>
    );
}

export default App;
