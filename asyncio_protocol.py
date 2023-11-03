import asyncio


# 创建http协议处理对象
class HttpProtocol(asyncio.Protocol):
    """
    asyncio 异步io协议 方法执行顺序：
    connection_made -> data_received -> eof_received -> connection_lost
    """
    # def __init__(self, loop: asyncio.get_event_loop()):
    #     self.loop = loop
    #     new_loop = asyncio.get_event_loop()
    #     print(loop, new_loop)
    #     self.transport = None
      

    def connection_made(self, transport):
        """
        连接建立时会调用的方法，
        :param transport transport可以理解为是一个 上下文，transport 对象中包含了客户端的链接信息
        """
        self.transport = transport       # 将上下文对象保存到对象属性中

    def data_received(self, data):
        """
        当创建完连接,执行完connection_made初始化的时候，会调用这个方法，将请求的数据传递到这里，
        在这里可以处理解析请求协议、路由、数据，
        :param data 就是请求的数据（二进制）
        """
        # 返回响应
        print(data.decode())
        response_data = "Reponse : " + data.decode()
        self.transport.write(response_data.encode())
        # self.transport.close()

    def eof_received(self):
        """
        有些请求是通过eof描述符来代表结束的， 遇到这种协议的请求时，会调用这个方法
        :return None:
        """

        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, exc):
        """
        请求结束收尾工作，不管有没有异常都会执行到
        :param exc: 参数 exc 是异常信息, 如果没有异常，exc 参数就是None
        :return:
        """
        pass

    def error_dispose(self, code):
        """
        :param code 错误响应码，在request_config 中配置有一些常见的错误
        """
        pass


async def run():
    host, port = "0.0.0.0", 8991
    loop = asyncio.get_event_loop()
    s = await loop.create_server(HttpProtocol, host=host, port=port)
    async with s:
        # 开启服务器事件循环
        await s.serve_forever()

asyncio.run(run())