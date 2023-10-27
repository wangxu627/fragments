// pixijs 处理被覆盖对象的事件监听

function setupScene() {
      const bunny = pixi.Sprite.from('https://pixijs.com/assets/bunny.png');
      const bunny2 = pixi.Sprite.from('https://pixijs.com/assets/bunny.png');

      // center the sprite's anchor point
      bunny.anchor.set(0.5);
      // move the sprite to the center of the screen
      bunny.x = 150;
      bunny.y = 150;
      bunny.interactive = true;
      bunny.on('pointerover', function (e) {
        console.log('1111111111111111111  iiiiiiiii');
      });
      // bunny.on('pointerout', function (e) {
      //   // bunny.interactive = true;
      //   // bunny2.interactive = true;
      //   console.log('1111111111111111111 ooooooooooo');
      // });

      const container = new pixi.Container();
      container.x = container.y = 0;
      // 创建一个Graphics对象来绘制斜线
      const graphics = new pixi.Graphics();
      graphics.lineStyle(2, 0xff0000); // 2像素宽，红色

      graphics.beginFill(0xde3249);
      // graphics.drawRect(50, 50, 100, 100);

      graphics.moveTo(0, 0);
      graphics.lineTo(200, 200);
      graphics.endFill();

      container.addChild(graphics);
      container.interactive = true;
      // container.hitArea = new pixi.Polygon([
      //   new pixi.Point(5, 0),
      //   new pixi.Point(205, 200),
      //   new pixi.Point(195, 200),
      //   new pixi.Point(0, 5)
      // ]);
      graphics.hitArea = new pixi.Polygon([
        new pixi.Point(5, 0),
        new pixi.Point(205, 200),
        new pixi.Point(195, 200),
        new pixi.Point(0, 5)
      ]);
      container.cursor = 'pointer';
      container.on('pointerover', function (event) {
        // console.log('EEEEEEEEEE ::: ', event);
        // const x = event.data.global.x; // 获取事件的全局X坐标
        // const y = event.data.global.y; // 获取事件的全局Y坐标
        // console.log(x, y);

        // console.log(graphics.containsPoint(new pixi.Point(x, y)));
        // console.log(graphics.getBounds());
        // console.log(container.getBounds());

        // console.log(container.getBounds().contains(x, y));

        // if (graphics.containsPoint(new pixi.Point(x, y))) {
        //   console.log('Pointer over graphics, but on sprite2');
        //   // container.emit('pointerover');
        // } else {
        //   console.log('Pointer over graphics');
        // }

        console.log('ccccccccccccccc  iiiiiiiii');
      });

      // center the sprite's anchor point
      bunny2.anchor.set(0.5);
      // move the sprite to the center of the screen
      bunny2.x = 150;
      bunny2.y = 150;
      bunny2.interactive = true;

      bunny2.on('pointerover', function (event) {
        // bunny2.interactive = false;

        const x = event.data.global.x; // 获取事件的全局X坐标
        const y = event.data.global.y; // 获取事件的全局Y坐标
        console.log(x, y);

        // 判断坐标是否位于 sprite2 上
        if (container.getBounds().contains(x, y)) {
          console.log('Pointer over sprite1, but on sprite2');
          container.emit('pointerover');
        } else {
          console.log('Pointer over sprite1');
        }
        console.log('2222222222222222 iiii , ', event, Date.now());

        if (bunny.containsPoint(new pixi.Point(x, y))) {
          console.log('Pointer over sprite1, but on sprite2');
          bunny.emit('pointerover');
        } else {
          console.log('Pointer over sprite1');
        }
        console.log('2222222222222222 iiii , ', event, Date.now());
      });
      // bunny2.on('pointerout', function (e) {
      //   // bunny.interactive = true;
      //   // bunny2.interactive = true;
      //   console.log('2222222222222222 ooooooooooo , ', e, Date.now());
      // });

      refs.stage.addChild(bunny);
      refs.stage.addChild(container);
      refs.stage.addChild(bunny2);
    }
