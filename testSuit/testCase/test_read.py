# @Time       :      2020/3/27 17:05
# @Description:

from log.logger import mylog
from testSuit.element_object.element import Element
import time
import unittest
class TestRead(Element):

    def test(self):
        x = self.get_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]')
        print(time.strftime("%Y-%m-%d %H-%M-%S"))
        self.action_func().long_press(x,1000).perform().release()
        print(time.strftime("%Y-%m-%d %H-%M-%S"))
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()