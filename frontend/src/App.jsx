import { lazy, Suspense } from 'react'
import { BrowserRouter, Routes, Route } from "react-router";
import Header from './shared/components/Header';

const Home = lazy(() => import('./pages/Home'))

function App() {
  return (
      <BrowserRouter>
        <Header />
        <main>
          <Suspense fallback={<div>Loading...</div>}>
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </Suspense>
        </main>
      </BrowserRouter>
  )
}

export default App